# conding=utf8

from rest_framework import serializers

# 引入model
from kpi_server.models import Users,Org,Reference,Index

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

class OrgSerializer(serializers.ModelSerializer):

    class Meta:

        model = Org
        # fields = '__all__'
        fields = ('org_num','org_name','org_group','org_level','parent_org_id','org_manager')

class RefSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reference
        # fields = '__all__'
        fields = ('ref_code','ref_name','ref_type')

class IndexSerializer(serializers.ModelSerializer):

    class Meta:

        model = Index
        # fields = '__all__'
        fields = ('index_num',)