# codingt=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.core.paginator import Paginator
from django.db.models import Q,Subquery
from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models.recUpload import UploadRecord
from kpi_server.models.userMain import Users
from kpi_server.serializers.uploadSerial import UploadRecordSerializer

import math,datetime

# 查询上传记录
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUploadList(request):

    # params解析
    query_params = {
        'record_class': int(request.query_params.get('class',0)),
        'start_date': request.query_params.get('start',None),
        'end_date': request.query_params.get('end',None),
        'key_word': request.query_params.get('key','all'),
        'record_date': request.query_params.get('date','all'),
        'user_client': request.query_params.get('client',None),
        'page_size': int(request.query_params.get('size',15)),
        'page': int(request.query_params.get('page',1))
    }

    # 参数检查
    if None in query_params.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        # 关键词匹配(用户名，notesid)
        if query_params['key_word'] == 'all':
            kw_condition = Q()
        else:
            kw_condition = Q(record_update_user__in=Subquery(Users.objects.filter(user_name__contains=query_params['key_word']).values('notes_id'))) \
                  | Q(record_update_user__contains=query_params['key_word']) | Q(record_id__contains=query_params['key_word'])

        # 分类匹配
        if query_params['record_class'] == 0:
            class_condition = Q()
        else:
            class_condition = Q(record_class=query_params['record_class'])

        # 归属月份判断
        if query_params['record_date'] == 'all':
            rd_condition = Q()
        else:
            rd_condition = Q(record_date=query_params['record_date'])

        # 上传记录匹配
        # 补充处理end日期
        date_value = datetime.datetime.strptime(query_params['end_date'],'%Y-%m-%d')
        query_params['end_date'] = datetime.datetime.combine(date_value,datetime.time(23,59,59))
        record_queryset = UploadRecord.objects.filter(
            record_update_time__range=[query_params['start_date'],query_params['end_date']]
        ).filter(rd_condition).filter(class_condition).filter(kw_condition).order_by('-record_update_time')

        # 分页
        page_inator = Paginator(record_queryset,query_params['page_size'])
        page_max = math.ceil(len(record_queryset)/query_params['page_size'])

        if query_params['page'] <= page_max:
            each_record_list = page_inator.page(query_params['page'])
            record_data = UploadRecordSerializer(each_record_list,many=True).data
            re_msg = {
                'code':200,
                'msg':settings.KPI_ERROR_MESSAGES['global'][200],
                'data':record_data,
                'has_next': (query_params['page']<page_max),
                'page_total': page_max,
                'page_no': query_params['page'],
                'data_total': len(record_queryset)
            }
        else:
            re_msg = {
                'code': 203,
                'msg':settings.KPI_ERROR_MESSAGES['global'][203]
            }

    return JsonResponse(re_msg,safe=False)