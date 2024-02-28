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
    rule_mark = models.CharField(help_text='模板备注',max_length=256)
    rule_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_rule_info'

# 考核指标信息
class ScoreRuleDetail(models.Model):

    detail_id = models.CharField(help_text='考核id',max_length=24,unique=True)
    parent_id = models.CharField(help_text='父级内容id',max_length=24)
    parent_class = models.IntegerField(help_text='父级内容类别')
    detail_level = models.IntegerField(help_text='考核指标等级')
    detail_wg_std = models.IntegerField(help_text='考核指标标准权重',blank=True)
    detail_wg_value = models.IntegerField(help_text='考核指标权重',blank=True)
    detail_wg_min = models.IntegerField(help_text='考核指标权重下限',blank=True)
    detail_wg_max = models.IntegerField(help_text='考核指标权重上限',blank=True)
    detail_sc_min = models.IntegerField(help_text='考核指标得分下限',blank=True)
    detail_sc_max = models.IntegerField(help_text='考核指标得分上线',blank=True)
    detail_ext_info = models.CharField(help_text='补充字段',max_length=512,blank=True)

    class Meta:

        app_label = 'kpi_server'
        db_table = 'score_rule_detail'

# 评价方式信息
class ScoreMethod(models.Model):

    method_id = models.CharField()