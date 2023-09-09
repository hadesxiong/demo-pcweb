# conding=utf8

from rest_framework import serializers

# 引入model
from kpi_server.models import Users,Org,Reference,Index,IndexDetail,Reference,UserAuth,DashboardMap,UploadRecord

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


class IndexDetailRank2Serializer(serializers.ModelSerializer):

    # 查询RefCode中index_class
    indexRef_queryset = Reference.objects.filter(ref_type='index_class').values('ref_code','ref_name')
    indexRef_dict = {item['ref_code']:item['ref_name'] for item in indexRef_queryset}

    # 查询Index,获取index_name
    index_queryset = Index.objects.all().values('index_num','index_name','index_class','belong_line')
    index_dict = {
        item['index_num']:{
            'index_name':item['index_name'],
            'index_class':item['index_class'],
            'belong_line':item['belong_line']
        }
        for item in index_queryset
    }

    # 查询Org,获取org_name
    org_queryset = Org.objects.all().values('org_num','org_name')
    org_dict = {item['org_num']:item['org_name'] for item in org_queryset}

    # 定义输出字段
    index_name = serializers.SerializerMethodField()
    index_class = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    belong_line = serializers.SerializerMethodField()
    org_name = serializers.SerializerMethodField()
    value_done = serializers.SerializerMethodField()
    value_rate = serializers.SerializerMethodField()

    def get_index_name(self,obj):
        return self.index_dict[obj['index_num']]['index_name']
    
    def get_index_class(self,obj):
        return self.index_dict[obj['index_num']]['index_class']
    
    def get_belong_line(self,obj):
        return self.index_dict[obj['index_num']]['belong_line']
    
    def get_class_name(self,obj):
        return self.indexRef_dict[self.index_dict[obj['index_num']]['index_class']]
    
    def get_org_name(self,obj):
        return self.org_dict[obj['detail_belong']]
    
    def get_value_done(self,obj):
        return obj['value_done']
    
    def get_value_rate(self,obj):
        return obj['value_rate']
    
    class Meta:
        
        model = IndexDetail
        # fields = '__all__'
        fields = ('index_num','index_name','belong_line','index_class','class_name','detail_belong','org_name','value_done','value_rate')

class RankSingleSerializer(serializers.Serializer):

    # 查询Org,获取org_name
    org_queryset = Org.objects.all().values('org_num','org_name')
    org_dict = {item['org_num']:item['org_name'] for item in org_queryset}

    # 定义输出字段
    detail_belong = serializers.SerializerMethodField()
    org_name = serializers.SerializerMethodField()
    value_tm_done = serializers.SerializerMethodField()
    value_ly_done = serializers.SerializerMethodField()
    value_compare = serializers.SerializerMethodField()
    value_ty_plan = serializers.SerializerMethodField()
    value_rate = serializers.SerializerMethodField()

    # 定义方法
    def get_detail_belong(self,obj):
        return obj['detail_belong']

    def get_org_name(self,obj):
        return self.org_dict[obj['detail_belong']]
    
    def get_value_tm_done(self,obj):
        return obj['value_tm_done']
    
    def get_value_ly_done(self,obj):
        return obj['value_ly_done']
    
    def get_value_compare(self,obj):
        return obj['value_compare']
    
    def get_value_ty_plan(self,obj):
        return obj['value_ty_plan']
    
    def get_value_rate(self,obj):
        return obj['value_rate']
    
    class Meta:

        model= IndexDetail
        # fields = '__all__'
        fields = ('detail_belong','org_name','value_tm_done','value_ly_done','value_compare','value_ty_plan','value_rate')

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = UserAuth
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class DashboardSerializer(serializers.ModelSerializer):

    class Meta:

        model = DashboardMap
        # fields = '__all__'
        fields = 'db_mark','db_name','db_class','index_num','db_func'

class UploadRecordSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()
    record_dt = serializers.SerializerMethodField()

    # 查询Users,获取user_name
    user_queryset = Users.objects.all().values('notes_id','user_name')
    user_dict = {item['notes_id']:item['user_name'] for item in user_queryset}

    def get_user_name(self,obj):
        return f'{obj.record_update_user} - {self.user_dict[obj.record_update_user]}'

    def get_record_dt(self,obj):
        return f'{obj.record_date.year}.{obj.record_date.month} - 通报数据'
    class Meta:

        model = UploadRecord
        # fields = '__all__'
        fields = ('record_id','record_class','record_dt','record_update_time','user_name')