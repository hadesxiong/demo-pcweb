# coding=utf8
from django.http.response import JsonResponse
from django.utils import timezone
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from kpi_server.models import UserAuth,UserToken

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64


# 通用方法 - 密码解密验证
def decrypt_aes(encrypted_data, key, iv):
    # 将 Base64 编码的加密数据解码为字节串
    encrypted_bytes = base64.b64decode(encrypted_data)
    # 初始化 AES 解密器
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    # 解密数据
    decrypted_data = decryptor.update(encrypted_bytes) + decryptor.finalize()
    # 去除填充
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    # 将解密后的字节串转换为字符串
    decrypted_text = unpadded_data.decode('utf-8')

    return decrypted_text

# token验证
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'You are authenticated!'})

# 用户登陆逻辑
@api_view(['POST'])
@permission_classes([AllowAny])
def userLogin(request):

    # 解析body
    body_data = {
        'notes_id': request.data.get('notes',None),
        'password': request.data.get('pw',None),
    }

    # 配置key,iv
    decrypt_key = bytes(settings.CRYPTO_KEY,'utf-8')
    decrypt_iv = bytes(settings.CRYPTO_IV,'utf-8')

    # 参数检查
    if None in body_data.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    # 登陆检查
    else:
        try:
            user = UserAuth.objects.get(notes_id=body_data['notes_id'])
            body_data['password'] = decrypt_aes(body_data['password'],decrypt_key,decrypt_iv)

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
                re_msg = {'code':100,'msg':settings.KPI_ERROR_MESSAGES['userLogin'][100]}
                response_obj = JsonResponse(re_msg,safe=False)
                response_obj['Access-Control-Expose-Headers'] = "*"
                response_obj['Authorization'] = f'Bearer {str(token.access_token)}'
                response_obj['X-Refresh-Token'] = token

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
                response_obj = JsonResponse(re_msg,safe=False)

        except UserAuth.DoesNotExist:
            re_msg = {'code':1,'msg':'no user found.'}
            response_obj = JsonResponse(re_msg,safe=False)

    return response_obj

# 用户注册逻辑
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userRegister(request):

    # 解析body
    body_data = {
        'notes_id': request.data.get('notes',None),
        'password': request.data.get('pw',None),
        'user_type': int(request.data.get('type',1))
    }

    # 配置key,iv
    decrypt_key = bytes(settings.CRYPTO_KEY,'utf-8')
    decrypt_iv = bytes(settings.CRYPTO_IV,'utf-8')

    # 参数检查
    if None in body_data.values():
        re_msg = {'code':0,'err_msg':'err params'}

    else:
        try:
            user = UserAuth.objects.get(notes_id=body_data['notes_id'])
            re_msg = {'code':1,'msg':'already exists'}

        except UserAuth.DoesNotExist:

            # 解密密码    
            body_data['password'] = decrypt_aes(body_data['password'],decrypt_key,decrypt_iv)

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