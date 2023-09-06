from django.urls import path
from kpi_server import views

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [

    # user
    path('api/user/getUserList',views.getUserList),
    path('api/user/updateUser',views.updateUser),
    path('api/user/createuser',views.createUser),

    # org
    path('api/org/getOrgList',views.getOrgList),
    path('api/org/updateOrg',views.updateOrg),

    # other
    path('api/other/getFilter',views.getFilter),
    path('api/other/generateDetail',views.generateDetail),

    # rank
    path('api/rank/getRank',views.getRankV2),
    path('api/rank/getSingleRank',views.getSingleRank),

    # table
    path('api/table/getTableData',views.getTableData),

    # jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # auth
    path('api/auth/newUser',views.newUser)
]