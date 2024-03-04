# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.db.models import Q
from django.conf import settings

from kpi_server.models.scoreMain import ScoreRuleInfo

from kpi_server.serializers.scoreSerial import ScoreRuleListSerial,ScoreRuleInfoSerial

from datetime import datetime,time

# 查询模板
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRuleList(request):

    # params解析
    query_params = {
        'state': int(request.query_params.get('state',0)),
        'start_dt':request.query_params.get('start',None),
        'end_dt':request.query_params.get('end',None),
        'key_word': request.query_params.get('key',None)
    }

    cleaned_query = {k: v for k, v in query_params.items() if v is not None}

    rl_query = Q()

    if cleaned_query.get('state') != 0: rl_query &= Q(rule_state=cleaned_query['state'])
    
    if cleaned_query.get('start_dt') and cleaned_query.get('end_dt'):

        date_value = datetime.strptime(cleaned_query['end_dt'],'%Y-%m-%d')
        cleaned_query['end_dt'] = datetime.combine(date_value,time(23,59,59))
        rl_query &= Q(rule_update_dt__range=[cleaned_query['start_dt'],cleaned_query['end_dt']])

    if cleaned_query.get('key_word'): rl_query &= Q(
        rule_name__contains=cleaned_query['key_word'],
        rule_update_usr__contains = cleaned_query['key_word'])

    rl_queryset = ScoreRuleInfo.objects.filter(rl_query).order_by('-rule_update_dt')

    rl_data = ScoreRuleListSerial(rl_queryset,many=True).data

    re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':rl_data}

    return JsonResponse(re_msg,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRuleInfo(request):

    # params解析
    query_params = {
        'rule_id': request.query_params.get('rule',None)
    }

    if None in query_params.values():
        re_msg = {'code':201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}
        return JsonResponse(re_msg,safe=False)
    
    else:
        try:
            rl_target = ScoreRuleInfo.objects.get(rule_id=query_params['rule_id'])
            rl_serial = ScoreRuleInfoSerial(rl_target)

            print(rl_serial.data)

            re_msg = {'code':0}

        except ScoreRuleInfo.DoesNotExist:
            re_msg = {'code':201,'msg':settings.KPI_ERROR_MESSAGES['global'][201]}

        return JsonResponse(re_msg,safe=False)