# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse

from kpi_server.models import IndexDetail,Index

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDashboard(request):

    # 解析query_params
    query_params = {
        'org_num': request.query_params.get('org',None),
        'start_date': request.query_params.get('start',None),
        'end_date': request.query_params.get('end',None),
        'index_type': request.query_params.get('index','all')
    }

    # 判断参数
    if None in query_params.values():
        re_msg = {'code':1,'msg':'err params.'}
    
    elif query_params['index_type'] == 'rtl_cb':

        rtl_cb_index = ['RC_001','RC_003','RC_004','RC_007']

        # 处理日期
        this_date = query_params['start_date']
        last_date = datetime.datetime.strptime(this_date,'%Y-%m-%d').date() - relativedelta(months=1)
        last_date = last_date.strftime("%Y-%m-%d")

        rtl_cb_queryset = IndexDetail.objects.filter(
            index_num__in=rtl_cb_index,
            detail_belong=query_params['org_num'],
            detail_date__range=[last_date,this_date],
            detail_type=2
        ).values('index_num','detail_value','detail_date')

        rtl_cb_df = pd.DataFrame(rtl_cb_queryset)

        rtl_cb_df_pivot= rtl_cb_df.pivot(index='index_num',columns='detail_date',values='detail_value').reset_index()

        rtl_cb_title = Index.objects.filter(index_num__in=rtl_cb_index).values('index_name','index_num','index_unit')

        print(rtl_cb_df_pivot)

        re_msg = {'code':0}

    return JsonResponse(re_msg,safe=False)