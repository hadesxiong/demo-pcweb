# coding=utf8
from django.db import models

# Token管理
class UserToken(models.Model):

    notes_id = models.CharField(max_length=8,unique=True,blank=False,help_text='用户notesid')
    rf_token_dt = models.DateTimeField(help_text='上次refresh_token刷新时间')
    ac_token_dt = models.DateTimeField(help_text='上次access_token刷新时间')
    rf_avalale = models.BooleanField(default=True,help_text='能否获取refresh_token')
    ac_avalale = models.BooleanField(default=True,help_text='能否获取refresh_token')
    login_err = models.IntegerField(default=0,help_text='登陆错误次数')

    class Meta:

        app_label = 'kpi_server'
        db_table = 'user_token'
    
# 用户表
class Users(models.Model):

    notes_id = models.CharField(max_length=8,blank=False,unique=True,help_text='用户notesid')
    user_name = models.CharField(max_length=64,blank=False,help_text='用户姓名')
    user_belong_org = models.CharField(max_length=10,help_text='用户归属机构')
    user_belong_group = models.IntegerField(help_text='用户所属分组/条线')
    user_character = models.IntegerField(help_text='用户角色')
    user_ext_info = models.CharField(max_length=64,help_text='用户信息补充字段')

    class Meta:

        app_label = 'kpi_server'
        db_table = 'user_info'
