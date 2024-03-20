# coding=utf8
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse
from django.db.models import Q
from django.conf import settings

from kpi_server.models.scoreMain import ScoreRuleInfo,ScoreRuleDetail,ScoreMethod
from kpi_server.utils.commonUtils import check_fields
from kpi_server.utils.updateForm import updateScoreConfig

from datetime import datetime

'''
更新考核方案信息，包含创建，修改，删除
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateScoreRule(request):

    # body解析
    body_data = {
        'update_type': request.data.get('type',None),
        'rule_id': request.data.get('rule',None),
        'rule_form': request.data.get('form',None)
    }

    cleaned_data = {k: v for k, v in body_data.items() if v is not None}

    '''
    创建逻辑，需要调用updateScoreDetail和updateScoreMethod
    '''

    if cleaned_data.get('update_type') == 'create':

        # 检查rule_info的基本字段
        try:

            rule_id = 'RI_' + str(int(datetime.now().timestamp()))

            rule_kwargs = {
                'rule_id': rule_id,
                'rule_name': cleaned_data['rule_form']['basic']['rule_name'],
                'rule_state': 1,
                'rule_update_dt': datetime.now(),
                'rule_update_usr': cleaned_data['rule_form']['basic']['rule_update_usr'],
                'rule_sum': cleaned_data['rule_form']['basic']['rule_sum'],
                'rule_mark': cleaned_data['rule_form']['basic']['rule_mark']
            } if check_fields(cleaned_data.get('rule_form').get('basic'),ScoreRuleInfo) else None
            
            # 检查子项detail的基本字段
            if cleaned_data.get('rule_form').get('detail') and len(cleaned_data.get('rule_form').get('detail')) !=0 :

                detail_list,method_list = updateScoreConfig(rule_id,cleaned_data['rule_form']['detail'])

                rule_info_ins = ScoreRuleInfo.objects.create(**rule_kwargs)

                detail_instances = [ScoreRuleDetail(**each_detail) for each_detail in detail_list]
                method_instances = [ScoreMethod(**each_method) for each_method in method_list]

                ScoreRuleDetail.objects.bulk_create(detail_instances)
                ScoreMethod.objects.bulk_create(method_instances)

                re_msg = {'code':300,'msg':settings.KPI_ERROR_MESSAGES['global'][300],'rule_id':rule_info_ins.rule_id}

            else:
                
                re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

        except Exception as error:

            re_msg = {'code':400,'msg':error}

    elif cleaned_data.get('update_type') == 'update':
        
        try:
            rule_target = ScoreRuleInfo.objects.filter(rule_id=cleaned_data['rule_id'])
            # 更新基本信息
            rule_info_form = cleaned_data.get('rule_form').get('basic')
            
            # 检查rule_info参数是否符合以及detail长度
            if (check_fields(rule_info_form,ScoreRuleInfo) and 
                cleaned_data.get('rule_form').get('detail') and
                len(cleaned_data.get('rule_form').get('detail')) !=0) :

                detail_list,method_list = updateScoreConfig(cleaned_data['rule_id'],cleaned_data['rule_form']['detail'])
                # 查找旧数据并删除，添加新数据
                origin_detail = ScoreRuleDetail.objects.filter(rule_id=cleaned_data['rule_id'],parent_id=cleaned_data['rule_id'])
                origin_method = ScoreMethod.objects.filter(detail_id__in=origin_detail.values('detail_id'))

                origin_method.delete()
                origin_detail.delete()

                detail_instances = [ScoreRuleDetail(**each_detail) for each_detail in detail_list]
                method_instances = [ScoreMethod(**each_method) for each_method in method_list]

                ScoreRuleDetail.objects.bulk_create(detail_instances)
                ScoreMethod.objects.bulk_create(method_instances)

                # 完成rule_info更新
                rule_info_form['rule_update_dt'] = datetime.now()
                rule_target.update(**rule_info_form)

                re_msg = {'code':301,'msg':settings.KPI_ERROR_MESSAGES['global'][301]}
            
            else:

                re_msg = {'code':304,'msg':settings.KPI_ERROR_MESSAGES['global'][304]}
        
        except ScoreRuleInfo.DoesNotExist:

            re_msg = {'code':305,'msg':settings.KPI_ERROR_MESSAGES['global'][305]}

        except Exception as error:

            re_msg = {'code':400,'msg':error}

    elif cleaned_data.get('update_type') == 'delete':

        try:
            rule_target = ScoreRuleInfo.objects.filter(rule_id=cleaned_data['rule_id'])
            rule_target.delete()

            # 查找detail及method
            detail_list = ScoreRuleDetail.objects.filter(rule_id=cleaned_data['rule_id'],parent_id=cleaned_data['rule_id'])
            method_list = ScoreMethod.objects.filter(detail_id__in=detail_list.values('detail_id'))

            method_list.delete()
            detail_list.delete()

            re_msg = {'code':302,'msg':settings.KPI_ERROR_MESSAGES['global'][302]}

        except ScoreRuleInfo.DoesNotExist:

            re_msg = {'code':305,'msg':settings.KPI_ERROR_MESSAGES['global'][305]}

        except Exception as error:

            re_msg = {'code':400,'msg':error}

    else:

        re_msg = {'code':202,'msg':settings.KPI_ERROR_MESSAGES['global'][202]}

    return JsonResponse(re_msg,safe=False)