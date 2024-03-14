# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.db.models import Q,F
from django.conf import settings

from kpi_server.models.scoreMain import ScoreRuleInstance
from kpi_server.serializers.scInsSerial import siListSerial,siInfoSerial

from datetime import datetime,time

# 查询列表
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getScoreInsList(request):

    # params解析
    query_params = {
        'state': int(request.query_params.get('state',0)),
        'org': request.query_params.get('org',None),
        'score_start': request.query_params.get('score_start',None),
        'score_end': request.query_params.get('score_end',None),
        'update_start': request.query_params.get('update_start',None),
        'update_end': request.query_params.get('update_end',None)
    }

    cleaned_query = {k: v for k, v in query_params.items() if v is not None}

    si_query = Q(instance_id=F('instance_parent'))

    if cleaned_query.get('state')!=0: si_query &= Q(instance_state=cleaned_query['state'])

    if cleaned_query.get('score_start') and cleaned_query.get('score_end'):

        sc_end_value = datetime.strptime(cleaned_query['score_end'],'%Y-%m-%d')
        cleaned_query['score_end'] = datetime.combine(sc_end_value,time(23,59,59))
        si_query &= Q(instance_period_st__lte=cleaned_query['score_start'],instance_period_end__gte=cleaned_query['score_end'])

    if cleaned_query.get('update_start') and cleaned_query.get('update_end'):

        update_end_value = datetime.strptime(cleaned_query['update_end'],'%Y-%m-%d')
        cleaned_query['update_end'] = datetime.combine(update_end_value,time(23,59,59))
        si_query &= Q(instance_update_dt__range=[cleaned_query['update_start'],cleaned_query['update_end']])

    si_queryset = ScoreRuleInstance.objects.filter(si_query).order_by('-instance_update_dt')
    si_data = siListSerial(si_queryset,many=True).data

    re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':si_data }

    return JsonResponse(re_msg,safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getScoreInsInfo(request):

    # params解析
    query_params = {
        'score_ins': request.query_params.get('ins',None)
    }

    if None in query_params.values():
        re_msg = {'code': 201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}
        return JsonResponse(re_msg,safe=False)
    
    else:
        try:
            si_target = ScoreRuleInstance.objects.filter(instance_parent=query_params['score_ins'])
            si_serial = siInfoSerial(si_target,many=True)
            re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':si_serial.data}

        except ScoreRuleInstance.DoesNotExist:
            re_msg = {'code':201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}

        return JsonResponse(re_msg,safe=False)