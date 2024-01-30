# coding=utf8
from django.db import models

# 指标信息表 - 用于维护指标本身
class Index(models.Model):

    index_num = models.CharField(help_text='指标编号',max_length=30,blank=False,unique=True)
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
    parent_index = models.CharField(help_text='上级指标',max_length=10,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'index_info'

# 指标详情表 - 用于记录机构/个人的单时间颗粒度指标记录
class IndexDetail(models.Model):

    detail_id = models.CharField(help_text='上传记录编号',max_length=48,blank=True)
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