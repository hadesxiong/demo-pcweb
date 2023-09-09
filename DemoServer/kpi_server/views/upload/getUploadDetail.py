# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q,Subquery

from django.http.response import JsonResponse

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
        re_msg = {'code':1,'msg':'err params'}

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
        record_data = UploadRecordSerializer(record_queryset,many=True).data

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

        print(merge_df)
        
        re_msg = {'code':0,'data':{'detail':detail_data,'info':record_data}}

    return JsonResponse(re_msg,safe=False)