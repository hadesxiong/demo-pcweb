# conding=utf8

from rest_framework import serializers

# 引入model
from kpi_server.models import Users,Org,Reference,Index,IndexDetail

# 引入基本方法
import math

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

# rank用指标序列化
class IndexDetailRankSerializer(serializers.ModelSerializer):

    index_num = serializers.CharField()
    detail_belong = serializers.CharField()
    detail_date = serializers.DateField()
    detail_value = serializers.DecimalField(max_digits=18,decimal_places=2)
    detail_plan = serializers.DecimalField(max_digits=18,decimal_places=2)
    detail_rate = serializers.FloatField()
    # 关联指标/机构等其他数据
    index_name = serializers.SerializerMethodField()
    org_name = serializers.SerializerMethodField()

    # 查询Index,获取index_name
    index_queryset = Index.objects.all().values('index_num','index_name')
    index_dict = {entry['index_num']: entry['index_name'] for entry in index_queryset}

    def get_index_name(self,obj):
        return self.index_dict[obj['index_num']]
    
    # 查询Org,获取org_name
    org_queryset = Org.objects.all().values('org_num','org_name')
    org_dict = {entry['org_num']:entry['org_name'] for entry in org_queryset}
    
    def get_org_name(self,obj):
        return self.org_dict[obj['detail_belong']]

    class Meta:

        model = IndexDetail
        # fields = '__all__'
        fields = ('index_num','detail_belong','detail_date','detail_value','index_name','org_name','detail_plan','detail_rate')

