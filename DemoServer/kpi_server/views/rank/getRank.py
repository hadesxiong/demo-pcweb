# conding=utf8
from rest_framework.decorators import api_view

from django.core.paginator import Paginator
from django.db import connections
from django.http.response import JsonResponse

from kpi_server.serializers import IndexDetailRankSerializer

import datetime,math

'''获取数据'''
# 获取数据接口较为负责，根据对应页面及功能进行区分
@api_view(['GET'])
def getRank(request):

    # params解析
    query_params = {
        # 'belong_line': request.query_params.get('line',0),
        'index_class': int(request.query_params.get('class',0)),
        'org_group': int(request.query_params.get('group',0)),
        'data_date': request.query_params.get('date',None),
        'page': int(request.query_params.get('page',1))
    }

    # 处理日期
    if None in query_params.values():
        syym = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        query_params['data_date'] = syym.strftime("%Y-%m-%d")

    # 指标筛选
    # 分类数据
    if query_params['index_class'] == 0:
        # index_condition = Q()
        # 后续补充动态
        index_condition = f'SELECT index_num FROM index_info WHERE index_class in (1,2,3,4,5)'
    else:
        # index_condition = Q(index_class=query_params['index_class'])
        index_condition = f'SELECT index_num FROM index_info WHERE index_class = {query_params["index_class"]}'

    # print(index_condition)

    # 是否重要数据补充
    
    # 机构筛选
    if query_params['org_group'] == 0:
        # group_condition = Q(org_group__gte=1) & Q(org_group__lte=3)
        group_condition = f'SELECT org_num FROM org_info WHERE org_group in (1,2,3)'
    else:
        # group_condition = Q(org_group=query_params['org_group'])
        group_condition = f'SELECT org_num FROM org_info WHERE org_group = {query_params["org_group"]}'

    # print(group_condition)

    # 获取计划筛选日期
    this_year = int(query_params['data_date'].split('-')[0])
    first_day = datetime.date(this_year,1,1).strftime("%Y-%m-%d")

    # 查询逻辑-sql
    set_var_query = '''
    SET @row_number := 0, @prev_index_num := NULL;
    '''
    
    get_data_query = f'''
    SELECT t.index_num, t.detail_belong, t.detail_date, t.detail_value AS result,
        (SELECT detail_value
            FROM index_detail AS d
            WHERE d.index_num = t.index_num
            AND d.detail_belong = t.detail_belong
            AND d.detail_date = '{first_day}'
            AND d.detail_type = 1
            ORDER BY d.detail_value DESC
            LIMIT 1) AS matching_detail_value
    FROM (
        SELECT 
            index_num, 
            detail_belong, 
            detail_date, 
            detail_value,
            CASE
                WHEN @prev_index_num = index_num THEN @row_number := @row_number + 1
                ELSE @row_number := 1
            END AS row_number,
            @prev_index_num := index_num
        FROM index_detail
        CROSS JOIN (SELECT @row_number := 0, @prev_index_num := NULL) AS vars
        WHERE (detail_date = '{query_params['data_date']}' 
            AND index_num IN ({index_condition}) 
            AND detail_belong IN ({group_condition}))
        ORDER BY index_num, detail_value DESC
    ) AS t
    WHERE t.row_number <= 5
    ORDER BY t.index_num, t.detail_value DESC;
    '''

    # 执行变量设定语句
    with connections['kpi_dashboard_db'].cursor() as cursor:
        cursor.execute(set_var_query)

    # 执行查询语句
    with connections['kpi_dashboard_db'].cursor() as cursor:
        cursor.execute(get_data_query)
        result = cursor.fetchall()

    # 结构化查询结果
    fetch_data = []
    for row in result:
        index_num,detail_belong,detail_date,detail_value,detail_plan = row
        fetch_data.append({
            'index_num':index_num,
            'detail_belong':detail_belong,
            'detail_date':detail_date,
            'detail_value':detail_value,
            'detail_plan':detail_plan,
            'detail_rate':round(detail_value/detail_plan,2)
        })
    # print(fetch_data)

    # 分页
    page_inator = Paginator(fetch_data,15)
    page_max = math.ceil(len(fetch_data)/15)

    if (query_params['page']<=page_max):
        each_rank_list = page_inator.page(query_params['page'])
        each_rank_data = IndexDetailRankSerializer(each_rank_list,many=True).data
        
        # merge data
        temp_dict = {}
        for item in each_rank_data:
            index_num = item['index_num']
            if index_num not in temp_dict:
                temp_dict.setdefault(index_num,{
                    'index_name':item['index_name'],
                    'index_num':index_num,
                    'detail_list':[]
                })

            temp_dict[index_num]['detail_list'].append({
                'detail_belong':item['detail_belong'],
                'detail_date':item['detail_date'],
                'detail_value':item['detail_value'],
                'detail_plan':item['detail_plan'],
                'detail_rate':item['detail_rate'],
                'org_name':item['org_name']
            })

        merge_data = list(temp_dict.values())

        re_msg = {'data': merge_data,'code':0,'msg':'success','has_next':(query_params['page']<page_max)}
    else:
        re_msg = {'code':1,'msg':'err range'}


    return JsonResponse(re_msg,safe=False)