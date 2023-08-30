# conding=utf8

from rest_framework import serializers

# 引入model
from kpi_server.models import Users


# 序列化
class UsersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Users
        fields = '__all__'