# coding=utf8
from rest_framework import serializers

from kpi_server.models.scoreMain import ScoreMethod

'''
评价标准序列化
用于查询评价方式序列化器
'''

class smListSerial(serializers.ModelSerializer):

    class Meta:

        model = ScoreMethod
        fields = ('method_id','method_title','method_desc','method_sc_min','method_sc_max','method_express')

        