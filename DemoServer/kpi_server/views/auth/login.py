# coding=utf8
from rest_framework.decorators import api_view,permission_classes

from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password

from kpi_server.models import UserAuth
from kpi_server.serializers import AuthSerializer

@api_view(['POST'])
def newUser(request):
    # permission_classes = (AllowAny,)

    # body解析
    body_data = {
        'user_name': request.data.get('user',None),
        'notes_id': request.data.get('notes',None),
        'password': request.data.get('pw',None)
    }

    body_data['password'] = make_password(body_data['password'])
    

    if None in body_data.values():
        re_msg = {'code':1,'msg':'err params.'}
    
    else:
        
        user_obj = UserAuth(**body_data)
        user_obj.save()
        re_msg = {'code':0,'msg':'success'}

    return JsonResponse(re_msg,safe=False)