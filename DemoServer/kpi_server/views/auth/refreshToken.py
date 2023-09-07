# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.http.response import JsonResponse

# 刷新token
@api_view(['POST'])
@permission_classes([AllowAny])
def refreshToken(request):

    # body解析
    body_data = {
        'refresh_token': request.data.get('refresh',None)
    }

    if None in body_data.values():
        re_msg = {'code':0,'err':'err params'}

    else:
        try:
            refresh = RefreshToken(body_data['refresh_token'])
            ac_token = str(refresh.access_token)
            re_msg = {'code':0,'access':ac_token}
        except Exception as e:
            re_msg = {'code':0,'err':str(e)}

    return JsonResponse(re_msg,safe=False)
        

