# coding=utf8

# 通用方法: 判断是否含有model定义以外的字段
def check_fields(dict_obj,model_obj):

    if not dict_obj:
        return False
    
    else:
        field_name = [f.name for f in model_obj._meta.get_fields() if not f.auto_created]
        undefined_fields = [f for f in dict_obj.keys() if f not in field_name]

        return len(undefined_fields) == 0