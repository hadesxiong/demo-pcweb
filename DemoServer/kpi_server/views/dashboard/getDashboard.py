# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse

from kpi_server.models import IndexDetail,Index,DashboardMap
from kpi_server.serializers import DashboardSerializer

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

# 通用方法定义 - 卡片数据
def getCardData(org_num,start_date,end_date,index_list):

    # 参数解释
    # org_num:机构编号
    # date:查询日期
    # index_list:指标数组

    # 处理日期
    this_date = end_date
    last_date = datetime.datetime.strptime(this_date,'%Y-%m-%d').date() - relativedelta(months=1,day=31)
    last_date = last_date.strftime("%Y-%m-%d")

    # 指标数据查询
    detail_queryset = IndexDetail.objects.filter(
        index_num__in = index_list,
        detail_belong = org_num,
        detail_date__range = [last_date,this_date],
        detail_type = 2
    ).values('index_num','detail_value','detail_date')

    # 引入pd对数据进行处理
    detail_df = pd.DataFrame(detail_queryset)
    detail_df['detail_date'] = detail_df['detail_date'].astype(str)
    detail_df_pivot = detail_df.pivot(index='index_num',columns='detail_date',values='detail_value').reset_index()

    title_queryset = Index.objects.filter(index_num__in=index_list).values('index_num','index_name','index_unit')
    title_df = pd.DataFrame(title_queryset)

    result_df = pd.merge(detail_df_pivot,title_df,on=['index_num'],how='left')
    result_df['value_compare'] = result_df[this_date] - result_df[last_date]

    result_df.drop(last_date,axis=1,inplace=True)
    result_df = result_df.rename(columns={this_date:'value_current','index_name':'card_title','index_unit':'value_unit'})
    result_df['value_status'] = result_df.apply(lambda x: 0 if x['value_compare'] <=0 else 1,axis=1)

    # data转换
    result_data = {'name':'','data':result_df.to_dict(orient='records')}

    return result_data

# 通用方法定义 - 柱状图/折线图
def getBarLineData(org_num,start_date,end_date,index_list):

    # 参数解释同上
    detail_queryset = IndexDetail.objects.filter(
        index_num__in = index_list,
        detail_belong = org_num,
        detail_date__range = [start_date,end_date],
        detail_type=2
    ).values('index_num','detail_value','detail_date')

    # 引入pd对数据进行处理
    detail_df = pd.DataFrame(detail_queryset)
    detail_df['detail_date'] = detail_df['detail_date'].astype(str)
    detail_df_pivot = detail_df.pivot(index='index_num',columns='detail_date',values='detail_value').reset_index()

    title_queryset = Index.objects.filter(index_num__in=index_list).values('index_num','index_name','index_unit')
    title_df = pd.DataFrame(title_queryset)

    # 拼接df,处理title
    result_df = pd.merge(detail_df_pivot,title_df,on=['index_num'],how='left')    
    title_df = result_df[['index_num','index_name']]

    # 处理result_df成为result_dict
    result_df.drop(['index_unit','index_name'],axis=1,inplace=True)
    result_df.set_index('index_num',inplace=True)
    result_dict = {}
    for index,row in result_df.iterrows():
        key = index
        values = row.values.tolist()
        result_dict[key] = values

    title_dict = title_df.to_dict(orient='records')

    # data处理
    result_data = {'name':title_dict,'data':result_dict}
    
    return result_data

# 定义db_func与方法的map
function_map = {
    'card_1': getCardData,
    'bar_1': getBarLineData,
    'line_1': getBarLineData
}

# 以下为接口方法

# 数据看板 - 单个
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDashboard(request):

    # 解析query_params
    query_params = {
        'org_num': request.query_params.get('org',None),
        'start_date': request.query_params.get('start',None),
        'end_date': request.query_params.get('end',None),
        'db_mark': request.query_params.get('mark',None)
    }

    # 判断参数
    if None in query_params.values():
        re_msg = {'code':1,'msg':'err params.'}

    elif query_params['db_mark'] == 'all':
        db_queryset = DashboardMap.objects.filter(db_state=1).values('db_mark','db_name','db_class','index_num','db_func')
        db_serializer = DashboardSerializer(db_queryset,many=True).data
        
        # 拉平所有index_num
        index_df = pd.DataFrame(db_serializer)
        index_list = index_df['index_num'].str.cat(sep=',').split(',')

        # 查询全量数据
        full_result = IndexDetail.objects.filter(
            index_num__in=index_list,detail_date__range=[query_params['start_date'],query_params['end_date']],
            detail_type=2,detail_belong=query_params['org_num']    
        ).values('index_num','detail_belong','detail_date','detail_value')
        full_df = pd.DataFrame(full_result)
        
        # 拉平df中的index_num
        db_df = pd.DataFrame(db_queryset)
        db_df['index_num'] = db_df['index_num'].str.split(',')
        db_df = db_df.explode('index_num')

        # 尝试合并
        merge_df = pd.merge(db_df,full_df,on=['index_num'],how='left')
        # 判断merge_df中的db_func，如果为card_1则取日期最大的一行值，如果不是则取全部
        filtered_df = merge_df[merge_df['db_func'] == 'card_1']

        filtered_df = filtered_df.groupby('index_num').apply(lambda x: x.loc[x['detail_date'].idxmax()])
        filtered_df = pd.concat([filtered_df, merge_df[merge_df['db_func'] != 'card_1']])

        filtered_df = filtered_df.reset_index(drop=True).groupby('db_mark')

        # 对过滤后的df按照目标格式进行处理
        # card_1: 按行取数形成对象，拼接数组即可
        # bar_1/line_1:  按index_num二次分组, 抽离出detail_date以及index_num，形成date/name两个公共部分

        result_data = {}
        for group_name,group_df in filtered_df:
            if group_df['db_func'] == 'card_1':
                each_result = {
                    ''
                }


        # grouped_df = filtered_df.groupby('db_mark')
        
        # for group_name,group_df in grouped_df:
        #     print(group_name)
        #     print(group_df)

        re_msg = {'code':0, 'data':{}}

    else:
        db_queryset = DashboardMap.objects.get(db_mark=query_params['db_mark'],db_state=1)
        index_list = db_queryset.index_num.split(',')
        func_type = db_queryset.db_func

        result_data = function_map[func_type](org_num = query_params['org_num'], start_date = query_params['start_date'],
            end_date = query_params['end_date'], index_list = index_list
        )
        re_msg = {'code':1,'msg':'done','title':db_queryset.db_name,'name':result_data['name'],'data':result_data['data'],'class':db_queryset.db_class}

    return JsonResponse(re_msg,safe=False)
