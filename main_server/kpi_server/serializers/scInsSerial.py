# coding=utf8
from rest_framework import serializers

from kpi_server.models.scoreMain import ScoreRuleDetail,ScoreRuleInstance
from kpi_server.models.userMain import Users
from kpi_server.models.orgMain import Org

from kpi_server.serializers.scDetailSerial import sdListSerial

'''
用于查询方案实例（模版）列表
'''
class siListSerial(serializers.ModelSerializer):

    ins_user = serializers.SerializerMethodField()
    ins_org = serializers.SerializerMethodField

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

'''
用于查询方案实例（模版）详情
'''
class siInfoSerial(serializers.ModelSerializer):

    ins_user = serializers.SerializerMethodField()
    ins_org = serializers.SerializerMethodField()
    score_detail = serializers.SerializerMethodField()

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
        
    def get_score_detail(self,obj):

        sd_target = ScoreRuleDetail.objects.filter(parent_id=obj.instance_id)
        sd_serial = sdListSerial(sd_target,many=True).data
        return sd_serial
    
    class Meta:

        model = ScoreRuleInstance
        fields = ('instance_id','rule_id','instance_parent','instance_state',
                  'instance_period_st','instance_period_end','instance_update_dt',
                  'score_detail','ins_user','instance_org','ins_org')