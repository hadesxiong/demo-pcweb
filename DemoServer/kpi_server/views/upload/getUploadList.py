# codingt=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q,Subquery

from django.http.response import JsonResponse

from kpi_server.models import UploadRecord,Users
from kpi_server.serializers import UploadRecordSerializer

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
        'record_date': request.query_params.get('date','all')
    }

    # 参数检查
    if None in query_params.values():
        re_msg = {'code':1,'msg':'err params.'}

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
        record_queryset = UploadRecord.objects.filter(
            record_update_time__range=[query_params['start_date'],query_params['end_date']]
        ).filter(rd_condition).filter(class_condition).filter(kw_condition)

        record_data = UploadRecordSerializer(record_queryset,many=True).data

        re_msg = {'code':0,'data':record_data}

    return JsonResponse(re_msg,safe=False)