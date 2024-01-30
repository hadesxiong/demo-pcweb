# coding=utf8
from django.db import models

# 指标上传记录
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

# 上传明细
class UploadDetail(models.Model):

    detail_id= models.CharField(help_text='历史记录编号',max_length=48,unique=True)
    record_id = models.CharField(help_text='上传记录编号',max_length=24)
    detail_active = models.IntegerField(help_text='该版本是否对外生效')
    detail_update_user = models.CharField(help_text='历史上传人员notesid',max_length=10)
    detail_update_fileName = models.CharField(help_text='历史记录上传文件名称',max_length=128)
    detail_update_fileMD5 = models.CharField(help_text='文件MD5值',max_length=128,default='')
    detail_state = models.IntegerField(help_text='历史记录状态')
    detail_create = models.DateField(help_text='创建时间',auto_now_add=True,auto_now=False)
    detail_update = models.DateField(help_text='修改时间',auto_now_add=False,auto_now=True)
    detail_ext_info = models.CharField(help_text='历史记录扩展字段',max_length=64)

    class Meta:
        
        app_label = 'kpi_server'
        db_table = 'upload_detail'
        