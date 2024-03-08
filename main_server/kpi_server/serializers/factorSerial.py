# coding=utf8
from rest_framework import serializers

from kpi_server.models.scoreMain import FactorConfig

'''
因子配置序列化
用于查询因子表达式
'''

class fctConfSerial(serializers.ModelSerializer):

    class Meta:
        
        model = FactorConfig
        fields = ('factor_id','factor_name','factor_class','factor_express')