# coding=utf8
from rest_framework import serializers

# 引入model
from kpi_server.models.indexMain import Index,IndexDetail
from kpi_server.models.orgMain import Org
from kpi_server.models.otherConf import Reference

import math

class IndexSerializer(serializers.ModelSerializer):

    class Meta:

        model = Index
        fields = ('index_num','index_name','index_class')

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
    children = serializers.SerializerMethodField()

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
    
    def get_children(self,obj):
        try:
            return obj['children']
        except:
            return None
    class Meta:

        model= IndexDetail
        # fields = '__all__'
        fields = ('detail_belong','org_name','value_tm_done','value_ly_done','value_compare','value_ty_plan','value_rate','children')

    def to_representation(self,instance):
        representation = super().to_representation(instance)

        if 'children' not in instance:
            representation.pop('children',None)
        
        return representation
    
class ScoreIndexDetailSerializer(serializers.ModelSerializer):

    # 查询所有org
    org_queryset = Org.objects.all().values('org_num','org_name')
    org_dict = {item['org_num']:item['org_name'] for item in org_queryset}

    # 查询所有index_name
    index_queryset = Index.objects.all().values('index_num','index_name')
    index_dict = {item['index_num']: item['index_name'] for item in index_queryset}

    index_name = serializers.SerializerMethodField()
    org_name = serializers.SerializerMethodField()
    detail_value = serializers.SerializerMethodField()

    def get_index_name(self,obj):
        return self.index_dict[obj['index_num']]
    
    def get_org_name(self,obj):
        return self.org_dict[obj['detail_belong']]
    
    def get_detail_value(self,obj):
        return math.floor(obj['detail_value'])


    class Meta:
        model = IndexDetail
        fields = ('detail_date','detail_belong','index_num','detail_value','index_name','org_name')