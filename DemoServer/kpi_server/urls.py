from django.urls import path
from kpi_server import views

urlpatterns = [
    path('api/userList',views.getUserList),
    path('api/updateUser',views.updateUser),
    path('api/createUser',views.createUser),
    path('api/orgList',views.getOrgList),
    path('api/updateOrg',views.updateOrg),
    path('api/getFilter',views.getFilter),
    path('api/generateDetail',views.generateDetail),
    path('api/getRank',views.getRank),
    path('api/getRankV2',views.getRankV2)
]