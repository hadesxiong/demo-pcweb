# conding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q,Subquery
from django.http.response import JsonResponse
from django.conf import settings

from kpi_server.models import IndexDetail,Users,Org,Index

import pandas as pd

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getTableData(request):

    # body解析
    body_data = {
        'index_num': request.data.get('index',None),
        'data_date': request.data.get('date',None),
        'org_group': request.data.get('group',None),
        # 'notes_id': request.data.get('user',None),
        'type': request.data.get('type','normal'),
        'parent_id': request.data.get('parent','2100001')
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

        # 根据用户所在层级判断 - 待补充

        detail_done_queryset = IndexDetail.objects.filter(
            index_num__in= body_data['index_num'],
            detail_type=2,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).filter(Q(detail_date__range=body_data['data_date'])).values('detail_date','detail_belong','index_num','detail_value')

        print(detail_done_queryset)
        dd_df = pd.DataFrame(detail_done_queryset)
    
        # done转置并重置索引
        dd_df_pivot = dd_df.pivot_table(index=['detail_date','detail_belong'],columns='index_num',values='detail_value')
        dd_df_pivot = dd_df_pivot.reset_index()

        # 添加suffix
        columns_to_suffix = body_data['index_num']

        # done转置添加后缀
        suffix_tm = '_tm'
        dd_df_pivot = dd_df_pivot.rename(columns={col:col+suffix_tm for col in columns_to_suffix})

        # 处理日期获取年份 - plan
        plan_year = list(map(lambda x:x.split('-')[0],body_data['data_date']))

        detail_plan_queryset = IndexDetail.objects.filter(
            index_num__in= body_data['index_num'],
            detail_type=1,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).filter(Q(detail_date__year__range=plan_year)).values('detail_date','detail_belong','index_num','detail_value')

        dp_df = pd.DataFrame(detail_plan_queryset)

        # plan转置并重置索引
        dp_df_pivot = dp_df.pivot_table(index=['detail_date','detail_belong'],columns='index_num',values='detail_value')
        dp_df_pivot = dp_df_pivot.reset_index()

        # plan转置添加后缀
        suffix_pl = '_pl'
        dp_df_pivot = dp_df_pivot.rename(columns={col:col+suffix_pl for col in columns_to_suffix})

        # 处理日期获取年份 - last
        last_year = list(map(lambda x:str(int(x.split('-')[0])-1),body_data['data_date']))

        detail_last_queryset = IndexDetail.objects.filter(
            index_num__in = body_data['index_num'],
            detail_type=2,
            detail_date__month=12,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).filter(Q(detail_date__year__range=last_year)).values('detail_date','detail_belong','index_num','detail_value')
        
        dl_df = pd.DataFrame(detail_last_queryset)

        # last转置并重置索引
        dl_df_pivot = dl_df.pivot_table(index=['detail_date','detail_belong'],columns='index_num',values='detail_value')
        dl_df_pivot = dl_df_pivot.reset_index()

        # last转置添加后缀
        suffix_ly = '_ly'
        dl_df_pivot = dl_df_pivot.rename(columns={col:col+suffix_ly for col in columns_to_suffix})

        dd_df_pivot['year'] = pd.to_datetime(dd_df_pivot['detail_date']).dt.year
        dp_df_pivot['year'] = pd.to_datetime(dp_df_pivot['detail_date']).dt.year
        dl_df_pivot['year'] = pd.to_datetime(dl_df_pivot['detail_date']).dt.year + 1

        # 合并dd_df,dp_df
        merge_df = pd.merge(dd_df_pivot,dp_df_pivot,on=['detail_belong','year'],how='left')
        merge_df = pd.merge(merge_df,dl_df_pivot,on=['detail_belong','year'],how='left')

        merge_df = merge_df.drop(columns=['year','detail_date','detail_date_y'])
        merge_df = merge_df.rename(columns={'detail_date_x':'detail_date'})

        # 增加两列计算结果
        for each_index in body_data['index_num']:
            merge_df[f'{each_index}_cp'] = round(merge_df[f'{each_index}_tm'].astype(float) - merge_df[f'{each_index}_ly'].astype(float),2)
            merge_df[f'{each_index}_rt'] = round((merge_df[f'{each_index}_tm'].astype(float) / merge_df[f'{each_index}_pl'].astype(float)) *100,2)

        # 补充org_name
        org_df = pd.DataFrame(org_queryset.values('org_num','org_name'))
        org_df = org_df.rename(columns={'org_num':'detail_belong'})

        # 合并
        merge_df = pd.merge(merge_df,org_df,on=['detail_belong'],how='left')

        # 处理表头
        ib_query = Index.objects.filter(index_num__in=body_data['index_num']).values('index_num','index_name','index_unit')
        ib_df = pd.DataFrame(ib_query)
        print(ib_df)

        # 处理顺序
        new_order = merge_df.columns.sort_values().tolist()
        new_order.remove('detail_belong')
        new_order.remove('detail_date')
        new_order.remove('org_name')
        new_order = ['detail_date','detail_belong','org_name'] + new_order
        
        merge_df = merge_df.reindex(columns=new_order).fillna('--')

        print(merge_df)

        # 处理表头
        title_list = [
            {'title':'数据月份','dataIndex':'detail_date','key':'detail_date','fixed':'left','width':120},
            {'title':'机构名称','dataIndex':'org_name','key':'org_name','fixed':'left','width':200}
        ]
        ct_map = {'cp':'期末比上年','tm':'期末','ly':'上年','pl':'计划','rt':'计划完成率'}

        for _,row in ib_df.iterrows():
            index_num = row['index_num']
            title = f"{row['index_name']}({row['index_unit']})"

            children_list = []
            # 遍历merge_df
            for column in merge_df.columns[3:]:
                if column.startswith(index_num):
                    dataIndex=column
                    key=column
                    column_title=''

                    # 查找对应的标题
                    column_title = ct_map[column[-2:]]
                    
                    # 创建子项的字典
                    child_dict = {
                        'dataIndex': dataIndex,
                        'key': key,
                        'title': column_title,
                        'width':100,
                        'align':'right'
                    }
                    children_list.append(child_dict)
            
            title_dict = {'title':title,'children':children_list}
            title_list.append(title_dict)

        # 处理成字典,orient=records
        df_list = merge_df.to_dict(orient='records')

    re_msg = {'data':df_list,'code':0,'title':title_list}
    
    return JsonResponse(re_msg,safe=False)