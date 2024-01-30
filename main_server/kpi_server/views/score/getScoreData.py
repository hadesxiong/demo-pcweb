# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import F,Subquery
from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models.indexMain import Index,IndexDetail
from kpi_server.serializers.indexSerial import ScoreIndexDetailSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getScoreData(request):

    query_params = {
        'org_num': request.query_params.get('org',None),
        'date': request.query_params.get('date',None)
    }

    # 参数判断
    if None in query_params.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        index_queryset = Index.objects.filter(belong_line=5,index_num=F('parent_index'))
        detail_queryset = IndexDetail.objects.filter(
            index_num__in=Subquery(index_queryset.values('index_num')),
            detail_belong=query_params['org_num'],
            detail_date=query_params['date'],
            detail_type=2
        ).values('index_num','detail_date','detail_belong','detail_value')
        detail_data = ScoreIndexDetailSerializer(detail_queryset,many=True).data

        re_msg = {'code':200,'msg': settings.KPI_ERROR_MESSAGES['global'][200],'data':detail_data}

    return JsonResponse(re_msg,safe=False)