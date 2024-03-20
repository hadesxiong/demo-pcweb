# coding=utf8
from kpi_server.models.scoreMain import ScoreRuleDetail,ScoreMethod
from kpi_server.utils.commonUtils import check_fields
from datetime import datetime

# 抽象写法：创建配置内容
def updateScoreConfig(rule_id,detail_form):

    detail_result = []
    method_result = []
    
    for each_detail in detail_form:

        detail_id = 'RD_' + str(int(datetime.now().timestamp()))

        detail_kwargs = {
            'detail_id': detail_id,
            'rule_id': rule_id,
            'parent_id': rule_id,
            'parent_class': each_detail.get('parent_class'),
            'detail_title': each_detail.get('detail_title'),
            'detail_level': each_detail.get('detail_level'),
            'detail_wg_std': each_detail.get('detail_wg_std'),
            'detail_wg_min': each_detail.get('detail_wg_min'),
            'detail_wg_max': each_detail.get('detail_wg_max'),
            'detail_sc_min': each_detail.get('detail_sc_min'),
            'detail_sc_max': each_detail.get('detail_sc_max')
        } if check_fields(
            {k:v for k,v in each_detail.items() if k!='method'},
            ScoreRuleDetail) else None
        
        # print(detail_kwargs)
        if detail_kwargs: detail_result.append(detail_kwargs)

        if each_detail.get('method') and len(each_detail.get('method')) != 0:

            for each_method in each_detail.get('method'):

                method_kwargs = {
                    'method_id': 'SM_' + str(int(datetime.now().timestamp())),
                    'detail_id': detail_id,
                    'method_title': each_method.get('method_title'),
                    'method_desc': each_method.get('method_desc'),
                    'method_sc_min': each_method.get('method_sc_min'),
                    'method_sc_max': each_method.get('method_sc_max'),
                    'method_express': each_method.get('method_express')
                } if check_fields(each_method,ScoreMethod) else None

                # print(method_kwargs)
                if method_kwargs: method_result.append(method_kwargs)

    return detail_result,method_result 