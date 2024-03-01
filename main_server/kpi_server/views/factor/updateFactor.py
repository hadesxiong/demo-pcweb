# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.db.models import Q,Subquery
from django.conf import settings

from kpi_server.models.scoreMain import FactorConfig
from kpi_server.utils.commonUtils import check_fields

from datetime import datetime

# 更新因子配置
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateFactor(request):

    # body解析
    body_data = {
        'mode': request.data.get('mode',None),
        'factor': request.data.get('factor',None),
        'form': request.data.get('form',None),
        'user': request.data.get('user',None)
    }

    cleaned_data = {k:v for k,v in body_data.items() if v is not None}

    # mode = 1,新建
    if cleaned_data.get('mode') == 1:

        try:
            factor_kwargs = {
                'factor_id': 'FC' + str(int(datetime.now().timestamp())),
                'factor_name': cleaned_data['form']['name'],
                'factor_class': cleaned_data['form']['class'],
                'factor_express': {
                    'factors': cleaned_data['form']['factors'],
                    'express': cleaned_data['form']['express']
                },
                'factor_update_dt': datetime.now(),
                'factor_update_usr': cleaned_data['user']
            } if check_fields(body_data['form'],FactorConfig) else None

            if factor_kwargs:
                factor_ins = FactorConfig.objects.create(**factor_kwargs)
                re_msg = {'code':300,'msg':settings.KPI_ERROR_MESSAGES['global'][300],'factor_id':factor_ins.factor_id}

            else:
                re_msg = {'code':304,'msg':settings.KPI_ERROR_MESSAGES['global'][304]}
            
            return JsonResponse(re_msg,safe=False)
        
        except Exception as error:

            re_msg = {'code':400,'msg':error}
            return JsonResponse(re_msg,safe=False)
        
    # mode = 2, 更新
    elif cleaned_data.get('mode') == 2:

        try:
            fc_target = FactorConfig.objects.filter(factor_id=cleaned_data['factor'])

            if check_fields(body_data['form'],FactorConfig):
                cleaned_data['form']['factor_update_dt'] = datetime.now()
                cleaned_data['form']['factor_update_usr'] = cleaned_data['user']
                fc_target.update(**cleaned_data['form'])
                re_msg = {'code':301,'msg':settings.KPI_ERROR_MESSAGES['global'][301]}

            else:
                re_msg = {'code':304,'msg':settings.KPI_ERROR_MESSAGES['global'][304]}

            return JsonResponse(re_msg,safe=False)
        
        except FactorConfig.DoesNotExist:

            re_msg = {'code':305,'msg':settings.KPI_ERROR_MESSAGES['global'][305]}

            return JsonResponse(re_msg,safe=False)
        
    else:
        re_msg = {'code':308,'msg':settings.KPI_ERROR_MESSAGES['global'][308]}
        return JsonResponse(re_msg,safe=False)