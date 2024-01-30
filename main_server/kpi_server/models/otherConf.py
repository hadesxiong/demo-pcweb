# coding=utf8
from django.db import models

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