# coding=utf8
from rest_framework import serializers

# 引入model
from kpi_server.models.otherConf import DashboardMap,Reference

class DashboardSerializer(serializers.ModelSerializer):

    class Meta:

        model = DashboardMap
        fields = 'db_mark','db_name','db_class','index_num','db_func'

class RefSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reference
        # fields = '__all__'
        fields = ('ref_code','ref_name','ref_type')
