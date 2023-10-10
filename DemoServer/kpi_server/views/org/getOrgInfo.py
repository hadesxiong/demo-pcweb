# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Subquery,Q

from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models import Org
from kpi_server.serializers import OrgSerializer

# 通用方法定义 - 树状结构机构
def build_tree(arr,son_level):
    son_arr = list(filter(lambda x:x['org_level']==son_level,arr))
    # 遍历
    result = {}
    for each in son_arr:
        if each['parent_org_id'] in result.keys():
            result[each['parent_org_id']].append({'org_num':each['org_num'],'org_name':each['org_name']})
        else:
            result[each['parent_org_id']] = [{'org_num':each['org_num'],'org_name':each['org_name']}]

    return result

'''查询机构信息'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrgInfo(request):

    # params解析
    query_params = {
        'type': request.query_params.get('type',None),
        'target': request.query_params.get('target',None),
        'group': request.query_params.get('group',0), 
    }

    # 参数检查
    if None in query_params.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        if query_params['type'] == 'single':
            org_queryset = Org.objects.filter(org_num=query_params['target'])
            org_data = OrgSerializer(org_queryset,many=True).data
            org_result = org_data[0] if len(org_data) > 0 else []

        elif query_params['type'] == 'tree':
            org_queryset = Org.objects.filter(org_group=query_params['group'])
            org_data = OrgSerializer(org_queryset,many=True).data

            if int(query_params['group']) == 1:
                parent_org = list(filter(lambda x: x['org_level']==3,org_data))
                parent_org = list(map(lambda x: {'org_num':x['org_num'],'org_name':x['org_name']},parent_org))
                son_org = build_tree(org_data,4)
                for each in parent_org:
                    try:
                        each['children'] = son_org[each['org_num']]
                    except:
                        pass
                org_result = parent_org
            
            else:
                org_result = list(map(lambda x: {'org_num':x['org_num'],'org_name':x['org_name']},org_data))

        re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':org_result}

    
    return JsonResponse(re_msg,safe=False)