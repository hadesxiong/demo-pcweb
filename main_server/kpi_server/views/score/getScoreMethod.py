# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models.scoreMain import ScoreMethod

from kpi_server.serializers.scMethodSerial import smListSerial

# 查询单一评价方式
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getScoreMethod(request):

    # params解析
    query_params = {
        'detail_id': request.query_params.get('detail',None)
    }

    if None in query_params.values():
        re_msg = {'code':201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}
        return JsonResponse(re_msg,safe=False)
    
    else:
        try:
            sm_target = ScoreMethod.objects.filter(detail_id=query_params['detail_id'])
            sm_serial = smListSerial(sm_target,many=True)
            re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':sm_serial.data}

        except ScoreMethod.DoesNotExist:
            re_msg = {'code':201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}

        return JsonResponse(re_msg,safe=False)