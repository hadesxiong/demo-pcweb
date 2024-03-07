# coding=utf8
from rest_framework import serializers

from django.db.models import F
# 引入model
from kpi_server.models.userMain import Users
from kpi_server.models.orgMain import Org
from kpi_server.models.scoreMain import FactorConfig,ScoreRuleInfo,ScoreRuleDetail,ScoreMethod,ScoreRuleInstance

class FactorConfSerial(serializers.ModelSerializer):

    class Meta:

        model = FactorConfig
        fields = ('factor_id','factor_name','factor_class','factor_express')

class ScoreRuleListSerial(serializers.ModelSerializer):

    rule_user = serializers.SerializerMethodField()

    def get_rule_user(self,obj):

        try:
            user_target = Users.objects.get(notes_id=obj.rule_update_usr)
            return f'{user_target.user_name} - {obj.rule_update_usr}'
        
        except Users.DoesNotExist:
            return ''


    class Meta:

        model = ScoreRuleInfo
        fields = ('rule_id','rule_name','rule_state','rule_update_dt','rule_user')

class ScoreMethodListSerial(serializers.ModelSerializer):

    class Meta:

        model = ScoreMethod
        fields = ('method_id','method_title','method_desc','method_sc_min','method_sc_max','method_express')

class ScoreDetailListSerial(serializers.ModelSerializer):
    
    class Meta:

        model = ScoreRuleDetail
        fields = (
            'detail_id','parent_id','parent_class','detail_level',
            'detail_wg_std','detail_wg_value','detail_wg_min','detail_wg_max',
            'detail_sc_min','detail_sc_max')


class ScoreRuleInfoSerial(serializers.ModelSerializer):

    score_detail = serializers.SerializerMethodField()
    rule_user = serializers.SerializerMethodField()

    def get_score_detail(self,obj):

        detail_obj = ScoreRuleDetail.objects.filter(rule_id=obj.rule_id,parent_id=F('rule_id'))
        return ScoreDetailListSerial(detail_obj,many=True).data
    
    def get_rule_user(self,obj):

        try:
            user_target = Users.objects.get(notes_id=obj.rule_update_usr)
            return f'{user_target.user_name} - {obj.rule_update_usr}'
        
        except Users.DoesNotExist:
            return ''

    class Meta:

        model = ScoreRuleInfo
        fields = ('rule_id','rule_name','rule_state','rule_update_dt','rule_user','rule_mark','score_detail')


class ScoreRuleInsListSerial(serializers.ModelSerializer):

    ins_user = serializers.SerializerMethodField()
    ins_org = serializers.SerializerMethodField()

    def get_ins_user(self,obj):

        try:
            user_target = Users.objects.get(notes_id=obj.instance_update_usr)
            return f'{user_target.user_name} - {obj.instance_update_usr}'
        
        except Users.DoesNotExist:
            return ''
        
    def get_ins_org(self,obj):

        try:
            org_target = Org.objects.get(org_num=obj.instance_org)
            return org_target.org_name
        except:
            return ''
    class Meta:

        model = ScoreRuleInstance
        fields = ('instance_id','rule_id','instance_parent','instance_state',
                  'instance_period_st','instance_period_end','instance_update_dt',
                  'ins_user','instance_org','ins_org')