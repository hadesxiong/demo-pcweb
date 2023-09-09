# codingt=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone

import uuid

# Create your models here.

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

# 机构表

class Org(models.Model):

    org_num = models.CharField(max_length=10,blank=False,unique=True,help_text='机构编号')
    org_name = models.CharField(max_length=64,blank=False,help_text='机构名称')
    parent_org_id = models.CharField(max_length=8,help_text='上级机构编号')
    org_level = models.IntegerField(help_text='机构层级')
    org_group = models.IntegerField(help_text='机构分组')
    org_manager = models.CharField(help_text='机构负责人id',max_length=8)
    org_create = models.DateTimeField(help_text='创建时间',auto_now_add=True,auto_now=False)
    org_update = models.DateTimeField(help_text='修改时间',auto_now_add=False,auto_now=True)
    org_state = models.IntegerField(help_text='机构状态')
    org_ext_info =  models.CharField(help_text='机构扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'org_info'

# 指标信息表 - 用于维护指标本身

class Index(models.Model):

    index_num = models.CharField(help_text='指标编号',max_length=10,blank=False,unique=True)
    index_class = models.IntegerField(help_text='指标分类-财务效益等')
    belong_line = models.IntegerField(help_text='归属条线-企金、零售、同业其他等')
    index_unit = models.CharField(help_text='指标单位',max_length=10)
    index_fre = models.IntegerField(help_text='指标频率')
    index_name = models.CharField(help_text='指标名称',max_length=64)
    index_type = models.IntegerField(help_text='指标类型-个人、机构')
    need_focus = models.IntegerField(help_text='是否重点指标')
    need_show = models.IntegerField(help_text='是否需要展示')
    is_db = models.IntegerField(help_text='是否首页数据看板')
    index_create = models.DateTimeField(help_text='创建时间',auto_now_add=False,auto_now=False)
    index_update = models.DateTimeField(help_text='修改时间',auto_now_add=False,auto_now=True)
    index_state = models.IntegerField(help_text='指标状态')
    index_ext_info = models.CharField(help_text='扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'index_info'

# 指标详情表 - 用于记录机构/个人的单时间颗粒度指标记录
class IndexDetail(models.Model):

    record_id = models.CharField(help_text='上传记录编号',max_length=10,blank=True)
    index_num = models.CharField(help_text='指标编号',max_length=10)
    detail_value = models.DecimalField(help_text='指标具体值',max_digits=18,decimal_places=2)
    detail_date = models.DateField(help_text='详情归属月份')
    detail_type = models.IntegerField(help_text='详情种类,是实际值还是计划值等')
    detail_class = models.IntegerField(help_text='详情归属，是个人还是机构')
    detail_belong = models.CharField(help_text='详情归属对象, 机构编号或者notesid',max_length=10)
    detail_create = models.DateTimeField(help_text='创建时间',auto_now_add=False,auto_now=False)
    detail_update = models.DateTimeField(help_text='修改时间',auto_now_add=False,auto_now=True)
    detail_state = models.IntegerField(help_text='详情状态')
    detail_ext_info = models.CharField(help_text='扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'index_detail'

class UploadRecord(models.Model):

    record_id = models.CharField(help_text='上传记录编号',max_length=24,unique=True)
    record_class = models.IntegerField(help_text='上传记录分类')
    record_date = models.DateField(help_text='上传归属时间')
    record_update_user = models.CharField(help_text='上传用户notesid',max_length=10)
    record_update_time = models.DateTimeField(help_text='上传时间',blank=False,auto_now=True)
    record_update_state= models.IntegerField(help_text='该条记录状态')
    record_create = models.DateTimeField(help_text='创建时间',auto_now_add=False,auto_now=False)
    record_update = models.DateTimeField(help_text='修改时间',auto_now_add=False,auto_now=True)
    record_update_ext_info = models.CharField(help_text='扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'upload_record'

class UploadDetail(models.Model):

    detail_id= models.CharField(help_text='历史记录编号',max_length=10,unique=True)
    record_id = models.CharField(help_text='上传记录编号',max_length=24)
    detail_active = models.IntegerField(help_text='该版本是否对外生效')
    detail_update_user = models.CharField(help_text='历史上传人员notesid',max_length=10)
    detail_update_fileName = models.CharField(help_text='历史记录上传文件名称',max_length=128)
    detail_state = models.IntegerField(help_text='历史记录状态')
    detail_create = models.DateField(help_text='创建时间',auto_now_add=True,auto_now=False)
    detail_update = models.DateField(help_text='修改时间',auto_now_add=False,auto_now=True)
    detail_ext_info = models.CharField(help_text='历史记录扩展字段',max_length=64)

    class Meta:
        
        app_label = 'kpi_server'
        db_table = 'upload_detail'

class Reference(models.Model):

    ref_name = models.CharField(help_text='码值含义',max_length=64)
    ref_code = models.IntegerField(help_text='码值')
    ref_type = models.CharField(help_text='码值用途',max_length=64)
    ref_state = models.IntegerField(help_text='是否有效')
    ref_ext = models.CharField(help_text='码值额外描述',max_length=128)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'reference_code'
        unique_together = (('ref_type','ref_code'))

class DashboardMap(models.Model):

    db_mark = models.CharField(help_text='看板标识',max_length=48)
    db_name = models.CharField(help_text='看板名称',max_length=128)
    db_class = models.IntegerField(help_text='数据分类')
    index_num = models.CharField(help_text='关联指标',max_length=256)
    db_func = models.CharField(help_text='对应方法',max_length=64)
    db_state = models.IntegerField(help_text='看板状态')
    db_ext = models.CharField(help_text='其他额外描述',max_length=128)
    db_create = models.DateTimeField(help_text='创建时间',auto_now_add=False,auto_now=False)
    db_update = models.DateTimeField(help_text='更新时间',auto_now_add=False,auto_now=False)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'dashboard_map'

class CodeMsg(models.Model):

    err_code = models.IntegerField(help_text='回复代码')
    code_type = models.IntegerField(help_text='代码分类')
    err_msg = models.CharField(help_text='错误信息',max_length=128)
    err_ext = models.CharField(help_text='额外内容',max_length=128)
    
    class Meta:

        app_label = 'kpi_server'
        db_table = 'code_msg'