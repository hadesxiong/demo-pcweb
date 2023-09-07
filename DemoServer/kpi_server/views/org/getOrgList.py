# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Subquery,Q
from django.core.paginator import Paginator
from django.http.response import JsonResponse

from kpi_server.models import Users,Org
from kpi_server.serializers import OrgSerializer

import math

'''查询机构列表'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrgList(request):

    # params解析
    query_params = {
        'org_level': int(request.query_params.get('level',0)),
        'org_group': int(request.query_params.get('group',0)),
        'key_word': request.query_params.get('ext',None),
        'user_client': request.query_params.get('client',None),
        'page_size':int(request.query_params.get('size',15)),
        'page':int(request.query_params.get('page',1))
    }

    # 分组筛选条件
    if query_params['org_group'] == 0:
        group_condition = Q()
    else:
        group_condition = Q(org_group=query_params['org_group'])

    # 层级筛选条件
    if query_params['org_level'] == 0:
        level_condition = Q()
    else:
        level_condition = Q(org_level=query_params['org_level'])

    # 关键词筛选
    if query_params['key_word'] is not None:
        complex_condition = Q(org_name__contains=query_params['key_word']) | Q(org_num__contains=query_params['key_word']) | Q(org_manager__in=Subquery(Users.objects.filter(notes_id__contains=query_params['key_word']).values('notes_id'))) | Q(org_manager__in=Subquery(Users.objects.filter(notes_id__contains=query_params['key_word']).values('notes_id')))
    else:
        complex_condition = Q()

    org_querySet = Org.objects.filter(group_condition).filter(level_condition).filter(complex_condition)

    # 分页
    page_inator = Paginator(org_querySet,query_params['page_size'])
    page_max = math.ceil(len(org_querySet)/query_params['page_size'])

    if query_params['page'] <= page_max:
        each_orgs_list = page_inator.page(query_params['page'])
        orgs_serializer = OrgSerializer(each_orgs_list,many=True)
        re_msg = {'data':orgs_serializer.data,'code':0,'msg':'success','has_next':(query_params['page']<page_max)}
    else:
        re_msg = {'code':1,'msg':'error_range'}

    return JsonResponse(re_msg,safe=False)