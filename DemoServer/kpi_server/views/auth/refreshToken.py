# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.http.response import JsonResponse
from django.conf import settings

# 刷新token
@api_view(['POST'])
@permission_classes([AllowAny])
def refreshToken(request):

    # body解析
    body_data = {
        'refresh_token': request.data.get('refresh',None)
    }

    if None in body_data.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        try:
            refresh = RefreshToken(body_data['refresh_token'])
            ac_token = str(refresh.access_token)
            re_msg = {
                'code':108,
                'msg':settings.KPI_ERROR_MESSAGES['refreshToken'][108],
                'access':ac_token
            }
        except Exception as e:
            re_msg = {
                'code':109,
                'msg': settings.KPI_ERROR_MESSAGES['refreshToken'][109]
            }

    return JsonResponse(re_msg,safe=False)
        

