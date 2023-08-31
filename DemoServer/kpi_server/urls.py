from django.urls import path
from kpi_server import views

urlpatterns = [
    path('api/usersList',views.getUsersList),
    path('api/updateUser',views.updateUser),
    path('api/createUser',views.createUser)
]