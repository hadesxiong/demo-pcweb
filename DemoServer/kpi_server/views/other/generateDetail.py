# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.http.response import JsonResponse

from kpi_server.models import Org,Index,IndexDetail
from kpi_server.serializers import IndexSerializer,OrgSerializer

import itertools

'''测试生成假数据'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generateDetail(request):

    # 解析body
    body_data = {
        'detail_type':request.data.get('type',None),
        'detail_class':request.data.get('class',1),
        'detail_date':request.data.get('date',None),
        'detail_belong':request.data.get('belong','all'),
        'index_num':request.data.get('index','all')
    }

    if None in body_data.values():
        re_msg = {'code':1,'msg':'err params.'}

    else:

        # 指标
        if body_data['index_num'] == 'all':
            index_list = IndexSerializer(Index.objects.all(),many=True).data
            grouped_index = itertools.groupby(index_list,lambda x:x['index_num'])
        
        body_data['index_num'] = [item['index_num'] for _,group in grouped_index for item in group]

        # 机构
        if body_data['detail_belong'] == 'all':
            org_queryset = Org.objects.filter(Q(org_level__gte=3) & Q(org_level__lt=5))
            org_data = OrgSerializer(org_queryset,many=True).data
            body_data['detail_belong'] = list(map(lambda x:x['org_num'],org_data))

        # print(list(map(lambda x:x['org_num'],org_data)))


        body_data['detail_create'] = body_data['detail_date']
        body_data['detail_state'] = [0]
        body_data['detail_value'] = [0]

        keys = body_data.keys()
        values = list(itertools.product(*body_data.values()))

        result = [{k:v for k,v in zip(keys,value)} for value in values]

        # for each_result in result:
        #     IndexDetail.objects.get_or_create(**each_result)

        objects = [IndexDetail(**item) for item in result]
        IndexDetail.objects.bulk_create(objects)

        re_msg = {'code':0,'msg':'done'}

    return JsonResponse(re_msg,safe=False)