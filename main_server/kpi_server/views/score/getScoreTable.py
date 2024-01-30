# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q,Subquery,F
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings

from kpi_server.models.indexMain import Index,IndexDetail
from kpi_server.models.orgMain import Org

import pandas as pd
import math

from datetime import datetime

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getScoreTable(request):

    body_data = {
        'index_num': request.data.get('index','all'),
        'data_date': request.data.get('date',None),
        'org_group': request.data.get('group',None),
        'type': request.data.get('type','normal'),
        'parent_id': request.data.get('parent','2100001'),
        'page': request.data.get('page',1),
        'size': request.data.get('size',0)
    }

    # 参数判断
    if None in body_data.values():
        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    else:
        
        # 机构筛选
        # 处理逻辑，获取当前登陆用户所在的机构

        if body_data['type'] == 'parent':
            org_queryset = Org.objects.filter(parent_org_id=body_data['parent_id'])

        elif body_data['org_group'] == 1:
            org_queryset = Org.objects.filter(org_group=body_data['org_group'],org_level=3)

        else:
            org_queryset = Org.objects.filter(org_group=body_data['org_group'])

        # 根据所用所在层级判断 - 待补充
            
        # 找出所有考核指标
        if body_data['index_num'] == 'all':
            index_queryset = Index.objects.filter(belong_line=5)
        else:
            index_queryset = Index.objects.filter(parent_index=body_data['index_num'])
        
        detail_queryset = IndexDetail.objects.filter(
            index_num__in = Subquery(index_queryset.values('index_num')),
            detail_type=2,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).filter(Q(detail_date__range=body_data['data_date'])).values('detail_date','detail_belong','index_num','detail_value')

        dd_df = pd.DataFrame(detail_queryset)

        # 转置并重置索引
        dd_df_pivot = dd_df.pivot_table(index=['detail_date','detail_belong'],columns='index_num',values='detail_value')
        dd_df_pivot = dd_df_pivot.reset_index()
        # print(dd_df_pivot)

        # 如果是区域中心支行，则增加树形数据
        if body_data['org_group'] == 1 and body_data['type'] == 'normal':
            dd_df_pivot['children'] = pd.Series([[]]*len(dd_df_pivot))

        # 补充org_name
        org_df = pd.DataFrame(org_queryset.values('org_num','org_name'))
        org_df = org_df.rename(columns={'org_num':'detail_belong'})

        # 补充index_name
        index_df = pd.DataFrame(index_queryset.values('index_num','index_name'))

        # 合并
        merge_df = pd.merge(dd_df_pivot,org_df,on=['detail_belong'],how='left')

        # 处理表头
        title_list = [
            {'title':'数据月份','dataIndex':'detail_date','key':'detail_date','fixed':'left','width':120},
            {'title':'机构名称','dataIndex':'org_name','key':'org_name','fixed':'left','width':220}
        ]

        # 如果是全部状态则添加一列计算结果总分
        if body_data['index_num'] == 'all':
            parent_index_queryset = Index.objects.filter(belong_line=5,parent_index=F('index_num')).values('index_num')
            parent_index = parent_index_queryset.values_list('index_num',flat=True)
            parent_cols = [str(num).zfill(3) for num in parent_index]
            merge_df['score_sum'] = round(merge_df[parent_cols].sum(axis=1).astype(float),2)
            # 添加进表头
            title_list.append(
                {'title':'考核评分总分','dataIndex':'score_sum','key':'score_sum','width':150}
            )


        # index形成一个df
        index_df = pd.DataFrame(index_queryset.values('index_num','index_name','parent_index'))
        print(index_df)

        index_dict = {}

        for _,row in index_df.iterrows():
            if row['parent_index'] == row['index_num']:
                index_dict[row['index_num']] = {'title':row['index_name'],'children':[]}

        for _,row in index_df.iterrows():
            if row['parent_index'] == row['index_num']:
                index_dict[row['index_num']]['children'].insert(0,{
                    'dataIndex': row['index_num'],
                    'key':row['index_num'],
                    'title': '总得分',
                    'width': "auto",
                    'align': 'right'
                })
            else:
                index_dict[row['index_num']]['children'].append({
                    'dataIndex': row['index_num'],
                    'key':row['index_num'],
                    'title': row['index_name'],
                    'width': "'auto'",
                    'align': 'right'
                })

        # 处理成字典,orient=records，如果type是parent的，需要先删除detail_date
        if body_data['type'] == 'parent':
            merge_df = merge_df.drop('detail_date',axis=1)
        df_list = merge_df.to_dict(orient='records')
                
        # normal下处理分页
        if body_data['type'] == 'normal':
            page_size = len(org_queryset) if body_data['size'] == 0 else body_data['size']
            if page_size <=6:
                print(page_size)
                page_size = page_size*2
            paginator = Paginator(df_list,page_size)
            page_max = math.ceil(len(df_list)/page_size)
            page = paginator.get_page(body_data['page'])

            if body_data['page'] <= page_max:
                current_page_data = page.object_list

                re_msg = {
                    'code': 200,
                    'msg': settings.KPI_ERROR_MESSAGES['global'][200],
                    'data': current_page_data,
                    'title': title_list + list(index_dict.values()),
                    'has_next': body_data['page'] < page_max,
                    'page_no': body_data['page'],
                    'page_total': page_max,
                    'data_total': len(df_list),
                    'dt_stamp': int(datetime.timestamp(datetime.now())*1000)
                }

            else:
                re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

        else:
            re_msg = {'code':200,'msg':settings.KPI_ERROR_MESSAGES['global'][200],'data':df_list}
    
    return JsonResponse(re_msg,safe=False)