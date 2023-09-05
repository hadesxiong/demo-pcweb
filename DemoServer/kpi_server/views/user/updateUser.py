# coding=utf8
from rest_framework.decorators import api_view

from django.http.response import JsonResponse

from kpi_server.models import Users

'''删除/更新用户信息'''

@api_view(['POST'])
def updateUser(request):

    # body解析
    body_data = {
        'type':request.data.get('type','update'),
        'notes_id':request.data.get('user',None),
        'update_data':request.data.get('update_data',None),
    }

    if body_data['notes_id'] is not None:
        user_obj = Users.objects.get(notes_id=body_data['notes_id'])

        if user_obj and  body_data['update_data'] is not None and (body_data['type'] == 'update'):
            for (x,y) in body_data['update_data'].items():
                print(x,y)
                setattr(user_obj,x,y)
            user_obj.save()
            re_msg = {'code':0,'msg':'update success'}

        elif user_obj and (body_data['type'] == 'delete'):
            user_obj.delete()
            re_msg = {'code':0,'msg':'delete success'}

        else:
            re_msg = {'code':1,'msg':'user not found'}

    else:
        re_msg = {'code':3,'msg':'error params.'}

    return JsonResponse(re_msg,safe=False)