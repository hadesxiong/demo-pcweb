# coding=utf8
from django.http.response import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from kpi_server.models import UserAuth,UserToken

# token验证
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'You are authenticated!'})

# 用户注册/登陆逻辑
@api_view(['POST'])
@permission_classes([AllowAny])
def userLogin(request):

    # 解析body
    body_data = {
        'notes_id': request.data.get('notes',None),
        'password': request.data.get('pw',None),
        'user_type': int(request.data.get('type',1))
    }

    # 参数检查
    if None in body_data.values():
        re_msg = {'code':0,'err_msg':'err params'}

    # 登陆检查
    else:
        try:
            user = UserAuth.objects.get(notes_id=body_data['notes_id'])
            if user.check_password(body_data['password']):
                # 验证通过，发放token
                token = RefreshToken.for_user(user)
                # 更新UserToken
                try:
                    user_token = UserToken.objects.get(notes_id=body_data['notes_id'])
                    user_token.rf_token_dt = timezone.now()
                    user_token.ac_token_dt = timezone.now()

                except UserToken.DoesNotExist:
                    user_token = UserToken(
                        notes_id=body_data['notes_id'],
                        rf_token_dt=timezone.now(),
                        ac_token_dt=timezone.now()    
                    )

                user_token.save()
                re_msg = {'code':0,'msg':'success','refresh':str(token),'access':str(token.access_token)}

            else:
                try:
                    user_token = UserToken.objects.get(notes_id=body_data['notes_id'])
                    user_token.login_err = user_token.login_err + 1
                
                except UserToken.DoesNotExist:
                    user_token = UserToken(
                        notes_id=body_data['notes_id'],
                        login_err = 1
                    )
                
                user_token.save()
                re_msg = {'code':1,'err':f'{user_token.login_err}次'}

        except UserAuth.DoesNotExist:
            
            # 普通用户
            if body_data['user_type'] == 1:
                normal_user = UserAuth.objects.createUser(
                    notes_id=body_data['notes_id'],
                    password=body_data['password']
                )
                # 发放token
                token = RefreshToken.for_user(normal_user)
                re_msg = {'code':0,'msg':'create success','type':'user','refresh':str(token),'access':str(token.access_token)}
    
            elif body_data['user_type'] == 2:
                admin_user = UserAuth.objects.createAU(
                    notes_id=body_data['notes_id'],
                    password=body_data['password']
                )
                # 发放token
                token = RefreshToken.for_user(admin_user)
                re_msg = {'code':0,'msg':'create success','type':'admin user','refresh':str(token),'access':str(token.access_token)}

            elif body_data['user_type'] == 3:
                super_user = UserAuth.objects.createSU(
                    notes_id=body_data['notes_id'],
                    password=body_data['password']
                )
                # 发放token
                token = RefreshToken.for_user(super_user)
                re_msg = {'code':0,'msg':'create success','type':'super user','refresh':str(token),'access':str(token.access_token)}
            else:
                re_msg = {'code':1,'msg':'err type'}

            

    return JsonResponse(re_msg,safe=False)