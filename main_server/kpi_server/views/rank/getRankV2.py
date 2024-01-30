# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Subquery,Q
from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models.orgMain import Org
from kpi_server.models.indexMain import Index,IndexDetail
from kpi_server.serializers.indexSerial import IndexDetailRank2Serializer


import datetime

'''获取排名数据'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRankV2(request):

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
        index_condition = ~Q(belong_line=5)
        # 后续补充动态
        # index_condition = f'SELECT index_num FROM index_info WHERE index_class in (1,2,3,4,5)'
    else:
        index_condition = Q(index_class=query_params['index_class']) & ~Q(belong_line=5)
        # index_condition = f'SELECT index_num FROM index_info WHERE index_class = {query_params["index_class"]}'

    # print(index_condition)

    # 是否重要数据补充
    
    # 机构筛选
    if query_params['org_group'] == 0:
        group_condition = Q(org_group__gte=1) & Q(org_group__lte=3)
        # group_condition = f'SELECT org_num FROM org_info WHERE org_group in (1,2,3)'
    else:
        group_condition = Q(org_group=query_params['org_group'])
        # group_condition = f'SELECT org_num FROM org_info WHERE org_group = {query_params["org_group"]}'

    # print(group_condition)

    # 获取计划筛选日期
    print(query_params['data_date'])
    this_year = int(query_params['data_date'].split('-')[0])
    first_day = datetime.date(this_year,1,1).strftime("%Y-%m-%d")

    # 查询逻辑
    done_queryset = IndexDetail.objects.filter(
        detail_date=query_params['data_date'],
        detail_belong__in=Subquery(Org.objects.filter(group_condition).values('org_num')),
        index_num__in=Subquery(Index.objects.filter(index_condition).values('index_num'))
    ).values('index_num','detail_belong','detail_value')

    plan_queryset = IndexDetail.objects.filter(
        detail_date=first_day,
        detail_belong__in=Subquery(Org.objects.filter(group_condition).values('org_num')),
        index_num__in=Subquery(Index.objects.filter(index_condition).values('index_num'))
    ).values('index_num','detail_belong','detail_value')

    rank_data = []

    for done,plan in zip(done_queryset,plan_queryset):
        index_num = done['index_num']
        detail_belong = done['detail_belong']
        value_done = done['detail_value']
        value_rate = round(done['detail_value']/plan['detail_value']*100,2)

        rank_data.append({
            'index_num':index_num,'detail_belong':detail_belong,'value_done':value_done,'value_rate':value_rate
        })

    rank_serializer = IndexDetailRank2Serializer(rank_data,many=True)
    rank_dataAll = rank_serializer.data

    # 数据筛选处理
    rankData_merged = []
    rankDict_merged = {}
    
    for item in rank_dataAll:
        key = (item["index_num"], item["index_name"], item["belong_line"], item["index_class"], item["class_name"])
        if key in rankDict_merged:
            rankDict_merged[key]["detail_list"].append({
                "detail_belong": item["detail_belong"],
                "org_name": item["org_name"],
                "value_done": item["value_done"],
                "value_rate": item["value_rate"]
            })
        else:
            rankDict_merged[key] = {
                "index_num": item["index_num"],
                "index_name": item["index_name"],
                "belong_line": item["belong_line"],
                "index_class": item["index_class"],
                "class_name": item["class_name"],
                "detail_list": [
                    {
                        "detail_belong": item["detail_belong"],
                        "org_name": item["org_name"],
                        "value_done": item["value_done"],
                        "value_rate": item["value_rate"]
                    }
                ]
            }

    rankData_merged = list(rankDict_merged.values())

    # 筛选+排序
    for item in rankData_merged:
        item["detail_list"] = sorted(item["detail_list"], key=lambda x: float(x["value_rate"]), reverse=True)[:5]

    rankData_group = {}
    for item in rankData_merged:
        new_key = item['belong_line']
        if item['belong_line'] in rankData_group.keys():
            del item['belong_line']
            rankData_group[new_key].append(item)
        else:
            del item['belong_line']
            rankData_group[new_key] = [item]

    table_columns = [
        {'title':'排名','dataIndex':'rank_sort','key':'rank_sort','width':'16%'},
        {'title':'机构名称','dataIndex':'org_name','key':'org_name'},
        {'title':'完成情况','dataIndex':'value_done','key':'value_done','align':'right'},
        {'title':'完成率','dataIndex':'value_rate','key':'value_rate','align':'right'}
    ]
    re_msg = {'code':200, 'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':rankData_group,'column':table_columns}

    return JsonResponse(re_msg,safe=False)