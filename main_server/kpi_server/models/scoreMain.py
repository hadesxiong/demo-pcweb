# coding=utf8
from django.db import models

# 模版基础信息
class ScoreRuleInfo(models.Model):

    rule_id = models.CharField(help_text='模板id',max_length=24,unique=True)
    rule_name = models.CharField(help_text='模板名称',max_length=128)
    rule_state = models.IntegerField(help_text='模板状态')
    rule_update_dt = models.DateTimeField(help_text='更新时间', auto_now_add=False,auto_now=False)
    rule_update_usr = models.CharField(help_text='更新人',max_length=24)
    rule_sum = models.IntegerField(help_text='模板总权重',blank=True)
    rule_mark = models.CharField(help_text='模板备注',max_length=256,blank=True,null=True)
    rule_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_rule_info'

# 考核指标分解
class ScoreRuleInstance(models.Model):

    instance_id = models.CharField(help_text='分解实例id',max_length=24,unique=True)
    rule_id = models.CharField(help_text='对应模版id',max_length=24)
    instance_parent = models.CharField(help_text='父级实例id',max_length=24)
    instance_state = models.IntegerField(help_text='实例状态')
    instance_period_st = models.DateTimeField(help_text='考核实例开始日期',auto_now=False,auto_now_add=False)
    instance_period_end = models.DateTimeField(help_text='考核实例结束日期',auto_now=False,auto_now_add=False)
    instance_org = models.CharField(help_text='实例归属机构',max_length=24)
    instance_update_dt = models.DateTimeField(help_text='实例更新日期',auto_now=False,auto_now_add=False)
    instance_update_usr = models.CharField(help_text='实例更新人员',max_length=24)
    instance_ext_info = models.CharField(help_text='扩展字段',max_length=512,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_rule_instance'

# 考核指标信息
class ScoreRuleDetail(models.Model):

    detail_id = models.CharField(help_text='考核id',max_length=24,unique=True)
    rule_id = models.CharField(help_text='对应模版id',max_length=24)
    parent_id = models.CharField(help_text='父级内容id',max_length=24,blank=True,null=True)
    parent_class = models.CharField(help_text='父级内容类别',max_length=96,blank=True,null=True)
    detail_title = models.CharField(help_text='考核指标名称',max_length=96)
    detail_level = models.IntegerField(help_text='考核指标等级')
    detail_wg_std = models.DecimalField(help_text='考核指标标准权重',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_wg_value = models.DecimalField(help_text='考核指标权重',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_wg_min = models.DecimalField(help_text='考核指标权重下限',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_wg_max = models.DecimalField(help_text='考核指标权重上限',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_sc_min = models.DecimalField(help_text='考核指标得分下限',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_sc_max = models.DecimalField(help_text='考核指标得分上线',max_digits=10,decimal_places=2,null=True,blank=True)
    detail_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_rule_detail'

# 评价方式信息
class ScoreMethod(models.Model):

    method_id = models.CharField(help_text='评价方式id',max_length=24)
    detail_id = models.CharField(help_text='关联考核指标id',max_length=24)
    method_title = models.CharField(help_text='评价方式名称',max_length=128)
    method_desc = models.CharField(help_text='评价方式描述',max_length=256)
    method_sc_min = models.DecimalField(help_text='评价方式得分下限',max_digits=10,decimal_places=2,null=True,blank=True)
    method_sc_max = models.DecimalField(help_text='评价方式得分上限',max_digits=10,decimal_places=2,null=True,blank=True)
    method_express = models.JSONField(help_text='计算表达式')
    method_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_method'

# 计算因子配置
class FactorConfig(models.Model):

    factor_id = models.CharField(help_text='因子id',max_length=24)
    factor_name = models.CharField(help_text='因子名称',max_length=128)
    factor_class = models.IntegerField(help_text='因子分类',default=1)
    factor_time_logic = models.IntegerField(help_text='时间逻辑',default=1)
    factor_org_logic = models.IntegerField(help_text='目标机构逻辑',default=1)
    factor_cal_logic = models.IntegerField(help_text='逻辑运算逻辑',default=1)
    factor_express = models.JSONField(help_text='因子计算表达式',max_length=512)
    factor_update_dt = models.DateTimeField(help_text='因子更新时间',auto_now_add=False,auto_now=False)
    factor_update_usr = models.CharField(help_text='因子更新人',max_length=24)
    factor_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True,null=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'factor_config'