# codingt=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models import Index,Reference
from kpi_server.serializers import IndexSerializer

from collections import defaultdict

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def getTableFilter(request):

    # params解析
    query_params = {
        'belong_line': int(request.query_params.get('line',None))
    }

    # 参数判断
    if None in query_params.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        # 根据传值找出目标指标
        index_queryset = Index.objects.filter(belong_line=query_params['belong_line'])
        index_data = IndexSerializer(index_queryset,many=True).data

        filter_data = defaultdict(list)

        for each in index_data:
            class_ = each['index_class']
            label = each['index_name']
            value = each['index_num']
            
            filter_data[class_].append({'label':label,'value':value})
        
        # 根据分类值找出对应分类
        ref_code = Reference.objects.filter(ref_type='index_class',ref_code__in=list(filter_data.keys())).values('ref_name','ref_code')
        index_class = [{'label':'全部','value':'all'}]
        for each in ref_code:
            index_class.append({'label':each['ref_name'],'value':each['ref_code']})

        index_list = [
            {'class':key,'label_list':value}
            for key,value in filter_data.items()
        ]

        index_list.insert(0, {
            'class': 'all',
            'label_list': [
                {'label': '全部', 'value': 'all'}
            ]
        })

        re_msg = {
            'code':200,
            'msg':settings.KPI_ERROR_MESSAGES['global'][200],
            'data':{'index_list':index_list,'index_class':index_class}
        }

    return JsonResponse(re_msg,safe=False)