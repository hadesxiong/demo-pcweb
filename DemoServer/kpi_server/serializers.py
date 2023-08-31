# conding=utf8

from rest_framework import serializers

# 引入model
from kpi_server.models import Users
from kpi_server.models import Org


# 序列化
class UsersSerializer(serializers.ModelSerializer):

    # 关联获取机构相关信息
    org_name = serializers.SerializerMethodField()
    org_manager = serializers.SerializerMethodField()

    def get_org_name(self,obj):

        org_obj = Org.objects.get(org_num=obj.user_belong_org)
        return org_obj.org_name
    
    def get_org_manager(self,obj):

        org_obj = Org.objects.get(org_num=obj.user_belong_org)
        return org_obj.org_manager
    
    
    class Meta:

        model = Users
        # fields = '__all__'
        fields = ('notes_id','user_name','user_character','user_belong_group','org_name','org_manager')