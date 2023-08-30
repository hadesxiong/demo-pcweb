from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from kpi_server.models import Users

from kpi_server.serializers import UsersSerializer
# Create your views here.

@api_view(['GET'])
def users_list(request):

    users_serializer = UsersSerializer(Users.objects.all(),many=True)
    re_msg = {'code':0,'data':users_serializer.data}

    return JsonResponse(re_msg,safe=False)