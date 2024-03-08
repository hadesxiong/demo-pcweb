# coding=utf8
from rest_framework import serializers

from django.db.models import F

from kpi_server.models.userMain import Users
from kpi_server.models.scoreMain import ScoreRuleInfo,ScoreRuleDetail

from kpi_server.serializers.scDetailSerial import sdListSerial

'''
方案信息序列化
用于查询方案列表
'''
class srListSerial(serializers.ModelSerializer):

    rule_user = serializers.SerializerMethodField()

    def get_rule_user(self,obj):

        try:
            user_target = Users.objects.get(notes_id=obj.rule_update_usr)
            return f'{user_target.user_name} - {obj.rule_update_usr}'
        
        except Users.DoesNotExist:
            return f'未知用户 - {obj.rule_update_usr}'
        
    class Meta:
        
        model = ScoreRuleInfo
        fields = ('rule_id','rule_name','rule_state','rule_update_dt','rule_user')

'''
方案详情序列化
用于查询单个方案下的详情，主要是各项子项信息
'''
class srInfoSerial(serializers.ModelSerializer):

    score_detail = serializers.SerializerMethodField()
    rule_user = serializers.SerializerMethodField()

    def get_score_detail(self,obj):

        detail_obj = ScoreRuleDetail.objects.filter(rule_id=obj.rule_id,parent_id=F('rule_id'))
        return sdListSerial(detail_obj,many=True).data
    
    def get_rule_user(self,obj):

        try:
            user_target = Users.objects.get(notes_id=obj.rule_update_usr)
            return f'{user_target.user_name} - {obj.rule_update_usr}'
        
        except Users.DoesNotExist:
            return ''

    class Meta:

        model = ScoreRuleInfo
        fields = ('rule_id','rule_name','rule_state','rule_update_dt','rule_user','rule_mark','score_detail')
