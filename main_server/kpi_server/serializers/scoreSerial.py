# coding=utf8
from rest_framework import serializers

# 引入model
from kpi_server.models.scoreMain import FactorConfig

class FactorConfSerial(serializers.ModelSerializer):

    class Meta:

        model = FactorConfig
        fields = ('factor_id','factor_name','factor_class','factor_express')