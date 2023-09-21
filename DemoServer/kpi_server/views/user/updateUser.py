# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models import Users

'''删除/更新用户信息'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
            re_msg = {'code':301,'msg':settings.KPI_ERROR_MESSAGES['global'][301]}

        elif user_obj and (body_data['type'] == 'delete'):
            user_obj.delete()
            re_msg = {'code':302,'msg':settings.KPI_ERROR_MESSAGES['global'][302]}

        else:
            re_msg = {'code':304,'msg':settings.KPI_ERROR_MESSAGES['global'][304]}

    else:
        re_msg = {'code':304,'msg':settings.KPI_ERROR_MESSAGES['global'][304]}

    return JsonResponse(re_msg,safe=False)