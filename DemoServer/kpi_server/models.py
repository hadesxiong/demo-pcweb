from django.db import models

# Create your models here.

# 用户表

class Users(models.Model):

    notes_id = models.CharField('用户notesid',max_length=8,blank=False,unique=True)
    user_name = models.CharField('用户姓名',max_length=64,blank=False)
    user_belong_org = models.CharField('用户归属机构',max_length=10)
    user_belong_group = models.IntegerField('用户所属分组/条线')
    user_character = models.IntegerField('用户角色')
    user_create = models.DateField('创建时间',blank=False,auto_now_add=True,auto_now=False)
    user_update = models.DateField('修改时间',auto_now_add=False,auto_now=False)
    user_states = models.IntegerField('用户状态')
    user_ext_info = models.CharField('用户信息补充字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'user_info'

# 机构表

class Org(models.Model):

    org_num = models.CharField('机构编号',max_length=10,blank=False,unique=True)
    org_name = models.CharField('机构名称',max_length=64,blank=False)
    parent_org_id = models.CharField('上级机构编号',max_length=8)
    org_level = models.IntegerField('机构层级')
    org_group = models.IntegerField('机构分组')
    org_manager = models.CharField('机构负责人id',max_length=8)
    org_create = models.DateField('创建时间',auto_now_add=True,auto_now=False,blank=False)
    org_update = models.DateField('修改时间',auto_now_add=False,auto_now=True)
    org_status = models.IntegerField('机构状态')
    org_ext_info =  models.CharField('机构扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'org_info'

# 指标信息表 - 用于维护指标本身

class Index(models.Model):

    index_num = models.CharField('指标编号',max_length=10,blank=False,unique=True)
    index_class = models.IntegerField('指标分类-财务效益等')
    belong_line = models.IntegerField('归属条线-企金、零售、同业其他等')
    index_unit = models.CharField('指标单位',max_length=10)
    index_name = models.CharField('指标名称',max_length=64)
    index_type = models.IntegerField('指标类型-个人、机构')
    need_focus = models.IntegerField('是否重点指标')
    need_show = models.IntegerField('是否需要展示')
    is_db = models.IntegerField('是否首页数据看板')
    index_create = models.DateField('创建时间',auto_now_add=True,auto_now=False,blank=False)
    index_update = models.DateField('修改时间',auto_now_add=False,auto_now=True)
    index_status = models.IntegerField('指标状态')
    index_ext_info = models.CharField('扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'index_info'

# 指标详情表 - 用于记录机构/个人的单时间颗粒度指标记录
class IndexDetail(models.Model):

    record_id = models.IntegerField('上传记录id')
    index_id = models.IntegerField('指标id')
    detail_date = models.DateField('详情归属月份')
    detail_type = models.IntegerField('详情种类,是实际值还是计划值等')
    detail_class = models.IntegerField('详情归属，是个人还是机构')
    detail_belong = models.CharField('详情归属对象, 机构编号或者notesid',max_length=10)
    detail_create = models.DateField('创建时间',auto_now_add=True,auto_now=False,blank=False)
    detail_update = models.DateField('修改时间',auto_now_add=False,auto_now=True)
    detail_status = models.IntegerField('详情状态')
    detail_ext_info = models.CharField('扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'index_detail'

class UploadRecord(models.Model):

    record_id = models.CharField('上传记录编号',max_length=10,unique=True)
    record_class = models.IntegerField('上传记录分类')
    record_name = models.CharField('上传记录名称',max_length=64)
    record_update_user = models.CharField('上传用户notesid',max_length=10)
    record_update_time = models.DateTimeField('上传时间',blank=False,auto_now=True)
    record_update_active = models.IntegerField('该条记录是否对外生效')
    record_update_status= models.IntegerField('该条记录状态')
    record_create = models.DateField('创建时间',auto_now_add=True,auto_now=False,blank=False)
    record_update = models.DateField('修改时间',auto_now_add=False,auto_now=True)
    record_update_ext_info = models.CharField('扩展字段',max_length=64)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'upload_record'

class UploadHistory(models.Model):

    history_id= models.CharField('历史记录编号',max_length=10,unique=True)
    record_name = models.CharField('上传记录名称',max_length=64)
    history_active = models.IntegerField('该版本是否对外生效')
    histroy_update_user = models.CharField('历史上传人员notesid',max_length=10)
    histroy_update_fileName = models.CharField('历史记录上传文件名称',max_length=128)
    histroy_status = models.IntegerField('历史记录状态')
    histroy_create = models.DateField('创建时间',auto_now_add=True,auto_now=False,blank=False)
    histroy_update = models.DateField('修改时间',auto_now_add=False,auto_now=True)
    histroy_ext_info = models.CharField('历史记录扩展字段',max_length=64)

    class Meta:
        
        app_label = 'kpi_server'
        db_table = 'upload_histroy'