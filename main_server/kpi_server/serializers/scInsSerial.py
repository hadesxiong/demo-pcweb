# coding=utf8
from rest_framework import serializers

from kpi_server.models.scoreMain import ScoreRuleDetail,ScoreRuleInstance
from kpi_server.models.userMain import Users
from kpi_server.models.orgMain import Org

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
        
