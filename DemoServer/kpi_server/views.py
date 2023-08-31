from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Subquery, Q

from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from kpi_server.models import Users, Org

from kpi_server.serializers import UsersSerializer

import math

# Create your views here.


@api_view(["GET"])
def getUsersList(request):
    # 请求参数解析
    query_params = {
        "belong_group": int(request.query_params.get("group", 0)),
        "user_character": int(request.query_params.get("character", 0)),
        "org_level": int(request.query_params.get("org", 0)),
        "key_word": request.query_params.get("ext", ""),
        "user_client": request.query_params.get("client", None),
        "page_size": int(request.query_params.get("size", 15)),
        "page": int(request.query_params.get("page", 1)),
    }

    # 筛选出机构层级
    org_query = Org.objects.filter(org_level=query_params["org_level"]).values(
        "org_num", "org_name"
    )

    # 关键词
    if query_params["key_word"] is not None:
        complex_condition = (
            Q(notes_id__contains=query_params["key_word"])
            | Q(user_name__contains=query_params["key_word"])
            | Q(
                user_belong_org__in=Subquery(
                    org_query.filter(
                        org_name__contains=query_params["key_word"]
                    ).values("org_num", "org_name")
                )
            )
        )

    else:
        complex_condition = Q()

    users_querySet = (
        Users.objects.filter(user_belong_org__in=Subquery(org_query.values("org_num")))
        .filter(user_belong_group=query_params["belong_group"])
        .filter(user_character=query_params["user_character"])
        .filter(complex_condition)
    )
    # users_querySet = Users.objects.all()

    # 分页
    page_inator = Paginator(users_querySet, query_params["page_size"])
    page_max = math.ceil(len(users_querySet) / query_params["page_size"])

    if query_params["page"] <= page_max:
        each_users_list = page_inator.page(query_params["page"])
        users_serializer = UsersSerializer(each_users_list, many=True)
        re_msg = {
            "data": users_serializer.data,
            "code": 0,
            "msg": "success",
            "has_next": (query_params["page"] < page_max),
        }
    else:
        re_msg = {"code": 1, "msg": "error_range"}

    return JsonResponse(re_msg, safe=False)
