# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.db.models import Q
from django.conf import settings

from kpi_server.models.scoreMain import FactorConfig
from kpi_server.serializers.scoreSerial import FactorConfSerial

# 查询因子配置
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFactorList(request):

    # params解析
    query_params = {
        'class': request.query_params.get('class',None),
        'key_word': request.query_params.get('key',None)
    }

    cleaned_query = {k: v for k, v in query_params.items() if v is not None}

    fl_query = Q()

    if cleaned_query.get('class'): fl_query &= Q(factor_class=cleaned_query['class'])
    if cleaned_query.get('key_word'): fl_query &= Q(factor_name__contains=cleaned_query['key_word'])

    fl_queryset = FactorConfig.objects.filter(fl_query).order_by('-factor_update_dt')
    
    fl_data = FactorConfSerial(fl_queryset,many=True).data

    re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':fl_data}

    return JsonResponse(re_msg,safe=False)