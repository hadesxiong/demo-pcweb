# coding=utf8
from rest_framework import serializers

# 引入models
from kpi_server.models.recUpload import UploadDetail,UploadRecord
from kpi_server.models.userMain import Users
from kpi_server.models.otherConf import Reference
from kpi_server.models.indexMain import IndexDetail

class UploadRecordSerializer(serializers.ModelSerializer):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # 查询Users,获取user_name
        user_queryset = Users.objects.all().values('notes_id','user_name')
        self.user_dict = {item['notes_id']:item['user_name'] for item in user_queryset}

        # 获取相关码值
        ref_queryset = Reference.objects.filter(ref_type__in=['belong_line']).values('ref_type','ref_code','ref_name')
        self.ref_dict = {f'{item["ref_type"]}_{item["ref_code"]}':item['ref_name'] for item in ref_queryset}

    user_name = serializers.SerializerMethodField()
    record_dt = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    record_update_time = serializers.DateTimeField("%Y-%m-%d - %H:%M:%S")

    def get_user_name(self,obj):
        return f'{obj.record_update_user} - {self.user_dict[obj.record_update_user]}'

    def get_record_dt(self,obj):
        return f'{obj.record_date.year}.{obj.record_date.month:02d}月 - 通报数据'
    
    def get_class_name(self,obj):
        return self.ref_dict[f'belong_line_{obj.record_class}']
    class Meta:

        model = UploadRecord
        fields = ('record_id','record_class','record_dt','record_date','record_update_time','user_name','class_name')

class UploadDetailSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()

    # 查询Users,获取user_name
    user_queryset = Users.objects.all().values('notes_id','user_name')
    user_dict = {item['notes_id']:item['user_name'] for item in user_queryset}

    def get_user_name(self,obj):
        return f'{obj.detail_update_user} - {self.user_dict[obj.detail_update_user]}'

    class Meta:
        model = UploadDetail
        fields = ('detail_id','detail_update','detail_active','detail_update_fileName','user_name')

class UploadIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndexDetail
        fields = ('detail_date','detail_belong','index_num','detail_value')