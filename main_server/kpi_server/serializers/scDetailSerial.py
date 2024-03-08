# coding=utf8
from rest_framework import serializers

from kpi_server.models.scoreMain import ScoreRuleDetail

'''
考核方案/考核实例，子项序列化器
用于查询某个考核方案/考核实例下所有的子项
'''
class sdListSerial(serializers.ModelSerializer):

    class Meta:

        model = ScoreRuleDetail
        fields = (
            'detail_id','parent_id','parent_class','detail_level',
            'detail_wg_std','detail_wg_value','detail_wg_min','detail_wg_max',
            'detail_sc_min','detail_sc_max')
        
'''

'''