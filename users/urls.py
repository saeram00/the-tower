from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.UserList.as_view(), name='Userlist'),
    path('detalle/<pk>', views.UserDetail.as_view(), name='Userdetail'),
    path('editar/<pk>', views.UserUpdate.as_view(), name='Userupdate'),
    path('eliminar/<pk>', views.UserDelete.as_view(), name='Userdelete'),
]
