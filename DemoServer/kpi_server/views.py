from django.shortcuts import render

from django.core.paginator import Paginator

from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from kpi_server.models import Users

from kpi_server.serializers import UsersSerializer

import math
# Create your views here.

@api_view(['GET'])
def getUsersList(request):

    query_params = {
        'belong_group': request.query_params.get('group',0),
        'user_character': request.query_params.get('character',0),
        'org_level': request.query_params.get('org',0),
        'key_word':request.query_params.get('ext',''),
        'user_client': request.query_params.get('client',None)
    }

    
    users_data_all = Users.objects.prefetch_related().all()
    # page_inator = Paginator(users_data_all,15)
    # page_max = math.cell(len(users_data_all)/15)

    users_serializer = UsersSerializer(Users.objects.all(),many=True)
    re_msg = {'code':0,'data':users_serializer.data}

    return JsonResponse(re_msg,safe=False)