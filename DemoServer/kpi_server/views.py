from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser

from kpi_server.models import Users

from kpi_server.serializers import UsersSerializer
# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):

    authentication_classes = []
    permission_classes = []

    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Users.objects.all
    serializer_class = UsersSerializer

    def list(self, request, *args, **kwargs):
        '''查询全部数据'''
        # return super().list(request, *args, **kwargs)
        users_list = UsersSerializer(Users.objects.all,many=True)
        re_msg = {'code':0,'data':users_list.data}

        return JsonResponse(re_msg,safe=False)
