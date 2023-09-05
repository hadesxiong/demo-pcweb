# conding=utf8
from rest_framework.decorators import api_view

from django.core.paginator import Paginator
from django.db.models import Subquery,Q
from django.http.response import JsonResponse

from kpi_server.models import Users,Org
from kpi_server.serializers import UsersSerializer

import math

'''查询用户列表'''

@api_view(['GET'])
def getUserList(request):

    # params解析
    query_params = {
        'belong_group': int(request.query_params.get('group',0)),
        'user_character': int(request.query_params.get('character',0)),
        'org_level': int(request.query_params.get('org',0)),
        'key_word':request.query_params.get('ext',None),
        'user_client': request.query_params.get('client',None),
        'page_size':int(request.query_params.get('size',15)),
        'page':int(request.query_params.get('page',1))
    }
    
    # 筛选出机构层级
    if query_params['org_level'] == 0:
        org_query = Org.objects.all().values('org_num','org_name')
    else:
        org_query = Org.objects.filter(org_level=query_params['org_level']).values('org_num','org_name')

    # 关键词
    if query_params['key_word'] is not None:
        complex_condition = Q(notes_id__contains=query_params['key_word']) | Q(user_name__contains=query_params['key_word']) | Q(user_belong_org__in=Subquery(Org.objects.filter(org_name__contains=query_params['key_word']).values('org_num')))
    else:
        complex_condition = Q()

    # 筛选用户所属条线
    if query_params['belong_group'] == 0:
        group_condition = Q()        
    else:
        group_condition = Q(user_belong_group=query_params['belong_group'])

    # 筛选用户角色
    if query_params['user_character'] == 0:
        character_condition = Q()
    else:
        character_condition = Q(user_character=query_params['user_character'])

    users_querySet = Users.objects.filter(user_belong_org__in=Subquery(org_query.values('org_num'))).filter(group_condition).filter(character_condition).filter(complex_condition)

    # 分页
    page_inator = Paginator(users_querySet,query_params['page_size'])
    page_max = math.ceil(len(users_querySet)/query_params['page_size'])

    if query_params['page'] <= page_max:
        each_users_list = page_inator.page(query_params['page'])
        users_serializer = UsersSerializer(each_users_list,many=True)
        re_msg = {'data':users_serializer.data,'code':0,'msg':'success','has_next':(query_params['page']<page_max)}
    else:
        re_msg = {'code':1,'msg':'error_range'}

    return JsonResponse(re_msg,safe=False)