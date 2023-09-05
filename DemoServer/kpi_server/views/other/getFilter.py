# coding=utf8
from rest_framework.decorators import api_view

from django.http.response import JsonResponse

from kpi_server.models import Reference
from kpi_server.serializers import RefSerializer

'''筛选项处理-处筛选'''
@api_view(['GET'])
def getFilter(request):

    # params解析
    query_params = {
        'ref_type': request.query_params.get('type',None),
        'ref_scene': int(request.query_params.get('scene',0)),
        'client': request.query_params.get('client','client')
    }

    if None in query_params.values():
        re_msg = {'code':1,'msg':'error params'}
    else:
        # 拆分ref_type
        type_list = query_params['ref_type'].split('.')
        ref_queryset = Reference.objects.filter(ref_ext__in=type_list)

        ref_serializer = RefSerializer(ref_queryset,many=True)
        ref_result = {}
        for each_ref in ref_serializer.data:
            ref_type = each_ref['ref_type']
            if ref_type not in ref_result:
                # setattr(ref_result,ref_type,{'ref_code':each_ref['ref_code'],'ref_name':each_ref['ref_name']})
                ref_result[ref_type] = []
            ref_result[ref_type].append({'ref_code':each_ref['ref_code'],'ref_name':each_ref['ref_name']})

        print(ref_result)

        re_msg = {'code':0,'data':ref_result}

    return JsonResponse(re_msg,safe=False)