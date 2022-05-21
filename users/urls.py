from django.urls import path
from . import views

urlpatterns = [
    # path('listado/', views.UserList.as_view(), name="Userlist"),
    # path('detalle/<pk>', views.UserDetail.as_view(), name="Userdetail"),
    path('registro/', views.register, name="Register"),
]
