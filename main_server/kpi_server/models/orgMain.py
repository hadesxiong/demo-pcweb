# coding=utf8
from django.db import models

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