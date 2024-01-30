# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse

from kpi_server.models.orgMain import Org

import datetime

'''新增/更新/删除机构'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateOrg(request):

    body_data = {
        'update_type': request.data.get('type','create'),
        'org_num': request.data.get('num',None),
        'update_data': request.data.get('update_data',None)
    }

    # 新增逻辑
    if body_data['update_type'] == 'create':
        # 表单
        update_data = {
            'org_num':body_data['org_num'],
            'org_name':body_data['update_data']['org_name'],
            'parent_org_id':body_data['update_data']['parent_org'],
            'org_level':body_data['update_data']['org_level'],
            'org_group':body_data['update_data']['org_group'],
            'org_manager':body_data['update_data']['org_manager'],
            'org_state':0,
            'org_create':datetime.date.today().strftime("%Y-%m-%d"),
            'org_update':datetime.date.today().strftime("%Y-%m-%d")
        }
        # 检验是否为空
        if None in update_data.values():
            re_msg = {'code':1,'msg':'err params'}

        else:
            obj,created = Org.objects.get_or_create(**update_data)
            if created:
                re_msg = {'code':0,'msg':'created','err':''}
            else:
                re_msg = {'code':1,'msg':'exists','err':''}

    # 更新逻辑
    elif body_data['update_type'] == 'update' and body_data['update_data'] is not None:

        try:
            org_obj = Org.objects.get(org_num=body_data['org_num'])
            for (x,y) in body_data['update_data'].items():
                setattr(org_obj,x,y)
            
            org_obj.save()
            re_msg = {'code':0,'msg':'updated','err':''}
        
        except Org.DoesNotExist:
            re_msg = {'code':1,'msg':'org not exists'}

    elif body_data['update_type'] == 'delete':

        try:
            org_obj = Org.objects.get(org_num=body_data['org_num'])
            org_obj.delete()

            re_msg = {'code':0,'msg':'deleted','err':''}
        
        except Org.DoesNotExist:
            re_msg = {'code':1,'msg':'org not exists'}

    return JsonResponse(re_msg,safe=False)