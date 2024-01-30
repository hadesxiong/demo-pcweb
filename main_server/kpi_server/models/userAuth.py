# coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone

import uuid

# 用户管理
class CustomUserManager(BaseUserManager):

    # 创建普通用户
    def createUser(self,notes_id,password=None):

        if not password:
            raise ValueError('password is required.')
        
        user = self.model(
            notes_id=notes_id,
            user_uuid=uuid.uuid4(),
            user_create=timezone.now(),
            user_update=timezone.now()
        )
        user.set_password(password)
        user.save()
        return user
    
    def createAU(self,notes_id,password=None):

        user = self.createUser(notes_id,password)
        user.is_admin = True
        user.save()
        return user

    # 创建超级用户
    def createSU(self,notes_id,password):

        user=self.createUser(notes_id,password)
        user.is_admin = True
        user.is_su= True
        user.save()
        return user
    
# 验证表
class UserAuth(AbstractBaseUser):

    notes_id = models.CharField(max_length=8,unique=True,help_text='用户notesid')
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_phone = models.CharField(max_length=16,default=0,help_text='手机号码')
    user_email = models.EmailField(help_text='用户邮箱')
    user_password = models.CharField(max_length=128,help_text='加密用户密码')
    user_state = models.IntegerField(default=0,help_text='用户状态')
    is_su = models.BooleanField(default=False, help_text='是否超级管理员')
    is_admin = models.BooleanField(default=False,help_text='是否普通管理员')
    user_create = models.DateTimeField(auto_now_add=False,auto_now=False,help_text='创建时间')
    user_update = models.DateTimeField(auto_now_add=False,auto_now=False,help_text='修改时间')

    password = None
    last_login = None

    # 其他字段

    objects = CustomUserManager()

    USERNAME_FIELD = 'notes_id'
    REQUIRED_FIELDS = ['user_uuid','password']

    def set_password(self,password):
        self.user_password = make_password(password)

    def check_password(self,password):
        return check_password(password,self.user_password)
    
    class Meta:
        app_label = 'kpi_server'
        db_table = 'user_auth'