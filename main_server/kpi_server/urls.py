# coding=utf8
from django.urls import path
from kpi_server import views

urlpatterns = [

    # user
    path('api/user/getUserList',views.getUserList),
    path('api/user/updateUser',views.updateUser),
    path('api/user/createUser',views.createUser),

    # org
    path('api/org/getOrgList',views.getOrgList),
    path('api/org/updateOrg',views.updateOrg),
    path('api/org/getOrgInfo',views.getOrgInfo),

    # other
    path('api/other/getFilter',views.getFilter),
    path('api/other/generateDetail',views.generateDetail),

    # rank
    path('api/rank/getRank',views.getRankV2),
    path('api/rank/getSingleRank',views.getSingleRank),

    # table
    path('api/table/getTableData',views.getTableData),
    path('api/table/getTableFilter',views.getTableFilter),

    # auth
    path('api/auth/userLogin',views.userLogin),
    path('api/auth/userRegister',views.userRegister),
    path('api/auth/refreshToken',views.refreshToken),
    path('api/auth/testToken',views.protected_view),
    path('api/auth/getUserInfo',views.getUserInfo),

    # dashboard
    path('api/dashboard/getDashboard',views.getDashboard),

    # upload
    path('api/upload/getUploadList',views.getUploadList),
    path('api/upload/getUploadDetail',views.getUploadDetail),
    path('api/upload/createUpload',views.createUpload),
    path('api/upload/publishUpload',views.publishUpload),

    #score
    path('api/score/getScoreTable',views.getScoreTable),
    path('api/score/getScoreData',views.getScoreData),
    path('api/score/getFactorList',views.getFactorList),
    path('api/score/updateFactor',views.updateFactor)
]