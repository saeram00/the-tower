from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.UserList.as_view(), name='Userlist'),
    path('perfil/<int:pk>', views.UserDetail.as_view(), name='Userdetail'),
    path('editar_datos/<int:pk>', views.UserUpdate.as_view(), name='Userupdate'),
    path('editar_foto/<int:pk>', views.ProfilePicUpdate.as_view(), name='Photoupdate'),
    path('eliminar/<int:pk>', views.UserDelete.as_view(), name='Userdelete'),
]
