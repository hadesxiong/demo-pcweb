# coding=utf8
from rest_framework import serializers

# 引入model
from kpi_server.models.userMain import Users
from kpi_server.models.otherConf import Reference
from kpi_server.models.orgMain import Org

class OrgSerializer(serializers.ModelSerializer):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # 一次性获取所需机构
        org_queryset = Org.objects.all().values('org_num','org_name','org_manager')
        self.org_dict = {item['org_num']:{'org_name':item['org_name']} for item in org_queryset}

        # 一次性获取相关码值
        ref_queryset = Reference.objects.filter(ref_type__in=['org_group','org_level']).values('ref_type','ref_code','ref_name')
        self.ref_dict = {f'{item["ref_type"]}_{item["ref_code"]}':item['ref_name'] for item in ref_queryset}

        # 一次性获取用户名称
        user_queryset = Users.objects.filter(user_character=3,user_belong_group=5).values('user_name','notes_id')
        self.user_dict = {item['notes_id']:f"{item['user_name']} - {item['notes_id']}" for item in user_queryset}

    # 补充字段定义
    group_name = serializers.SerializerMethodField()
    level_name = serializers.SerializerMethodField()
    parent_org_name = serializers.SerializerMethodField()
    org_manager_name = serializers.SerializerMethodField()

    def get_group_name(self,obj):
        return self.ref_dict[f'org_group_{obj.org_group}']
    
    def get_level_name(self,obj):
        return self.ref_dict[f'org_level_{obj.org_level}']
    
    def get_parent_org_name(self,obj):
        try:
            return self.org_dict[obj.parent_org_id]['org_name']
        except:
            return ''
    def get_org_manager_name(self,obj):
        try:
            return self.user_dict[obj.org_manager]
        except:
            return '暂无'

    class Meta:

        model = Org
        # fields = '__all__'
        fields = ('org_num','org_name','org_group','org_level','parent_org_id','org_manager','group_name','level_name','parent_org_name','org_manager_name')
