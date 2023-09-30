# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q,Subquery

from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models import UploadDetail,UploadRecord,IndexDetail,Index,Org
from kpi_server.serializers import UploadDetailSerializer,UploadRecordSerializer

import pandas as pd

# 查询上传明细
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUploadDetail(request):

    # params解析
    query_params = {
        'record_id': request.query_params.get('record',None)
    }

    # 参数检查
    if None in query_params.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        # 获取detail列表
        detail_queryset = UploadDetail.objects.filter(
            record_id=query_params['record_id'],
            detail_state=1
        )
        detail_data = UploadDetailSerializer(detail_queryset,many=True).data
        detail_data = sorted(detail_data,key=lambda x:x['detail_id'],reverse=True)

        # 获取基本信息
        record_queryset = UploadRecord.objects.filter(record_id=query_params['record_id'])
        record_data = UploadRecordSerializer(record_queryset,many=True).data[0]

        # 获取数据，排序获取最新的数据
        index_queryset = IndexDetail.objects.filter(
            detail_id=detail_data[0]['detail_id']
        ).values('detail_date','detail_belong','index_num','detail_value')

        org_queryset = Org.objects.filter(org_num__in=Subquery(index_queryset.values('detail_belong'))).values('org_num','org_name')
        ib_queryset = Index.objects.filter(index_num__in=Subquery(index_queryset.values('index_num'))).values('index_num','index_name','index_unit')

        # 数据整合形成宽表
        merge_df = pd.DataFrame(index_queryset).rename(columns={'detail_belong':'org_num'})
        merge_df = pd.merge(merge_df,pd.DataFrame(org_queryset),on=['org_num'],how='left')
        merge_df = pd.merge(merge_df,pd.DataFrame(ib_queryset),on=['index_num'],how='left')

        # 通过df转置
        pivot_df = pd.pivot(merge_df,values='detail_value',index=['detail_date','org_name'],columns=['index_num']).reset_index()

        index_data = pivot_df.to_dict(orient='records')
        
        # 拼接表头
        filter_df = merge_df[['detail_date','org_name','index_num']].drop_duplicates()
        
        header_list = [{'dataIndex':'detail_date','key':'detail_date','title':'数据日期'},{'dataIndex':'org_name','key':'org_name','title':'机构名称'}]
        print(filter_df)
        print(merge_df)
        for _, row in filter_df.iterrows():
            header_dict = {
                'dataIndex': row['index_num'],
                'key': row['index_num'],
                'title': merge_df.loc[(merge_df['index_num'] == row['index_num']) & (merge_df['org_name'] == row['org_name']), 'index_name'].values[0] + f"({merge_df.loc[(merge_df['index_num'] == row['index_num']) & (merge_df['org_name'] == row['org_name']), 'index_unit'].values[0]})"
            }
            header_list.append(header_dict)

        header_list = list(set(tuple(item.items()) for item in header_list))
        header_list = [dict(item) for item in header_list]

        # 表头排序
        header_list = sorted(header_list,key=lambda item:(0 if item['dataIndex'] == 'org_name' else 1, 0 if item['dataIndex'] == 'detail_date' else 1))

        re_msg = {
            'code':200,
            'data':{
                'detail':detail_data,
                'info':record_data,
                'title':header_list,
                'index':index_data
            },
            'msg': settings.KPI_ERROR_MESSAGES['global'][200]
        }

    return JsonResponse(re_msg,safe=False)