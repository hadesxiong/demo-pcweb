# coding=utf8
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate,login,logout
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def userLogin(request):

    # body_data解析
    body_data = {
        'user_name':request.data.get('user',None),
        'password': request.data.get('password',None)
    }

    user = authenticate(request,username=body_data['user_name'],password=body_data['password'])

    if user is not None:
        login(request,user)
        re_msg = {'code':0,'msg':'success'}

    else:
        re_msg = {'code':1,'msg':'fail'}

    return JsonResponse(re_msg,safe=False)
