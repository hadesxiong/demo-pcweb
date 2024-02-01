# coding=utf8
from rest_framework import serializers

# 引入model
from kpi_server.models.userAuth import UserAuth
from kpi_server.models.userMain import Users
from kpi_server.models.orgMain import Org
from kpi_server.models.otherConf import Reference

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAuth
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class UsersSerializer(serializers.ModelSerializer):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # 一次性获取所需机构
        org_queryset = Org.objects.all().values('org_num','org_name','org_manager')
        self.org_dict = {item['org_num']:{'org_name':item['org_name'],'org_manager':item['org_manager']} for item in org_queryset}

        # 获取相关码值
        ref_queryset = Reference.objects.filter(ref_type__in=['user_belong_group','user_character']).values('ref_type','ref_code','ref_name')
        self.ref_dict = {f'{item["ref_type"]}_{item["ref_code"]}':item['ref_name'] for item in ref_queryset}

        # 获取所有部门负责人
        manager_querysett = Users.objects.filter(user_character=3).values('notes_id','user_name')
        self.manager_dict = {item['notes_id']:item['user_name'] for item in manager_querysett}

    # 关联获取机构相关信息
    org_name = serializers.SerializerMethodField()
    org_manager = serializers.SerializerMethodField()

    # 补充角色信息及分组信息
    character_name = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()

    user_name_withId = serializers.SerializerMethodField()
    org_manager_withName = serializers.SerializerMethodField()

    def get_org_name(self,obj):
        return self.org_dict[obj.user_belong_org]['org_name']
    
    def get_org_manager(self,obj):
        return self.org_dict[obj.user_belong_org]['org_manager']
    
    def get_character_name(self,obj):
        return self.ref_dict[f'user_character_{obj.user_character}']
    
    def get_group_name(self,obj):
        return self.ref_dict[f'user_belong_group_{obj.user_belong_group}']
    
    def get_user_name_withId(self,obj):
        return f'{obj.user_name} - {obj.notes_id}'
    
    def get_org_manager_withName(self,obj):
        try:
            return f'{self.manager_dict[self.org_dict[obj.user_belong_org]["org_manager"]]} - {self.org_dict[obj.user_belong_org]["org_manager"]}'
        except:
            return ''
        
    class Meta:

        model = Users
        # fields = '__all__'
        fields = ('notes_id','user_name','user_character','user_belong_group', 'user_belong_org', 'org_name','org_manager','character_name','group_name','user_name_withId','org_manager_withName')