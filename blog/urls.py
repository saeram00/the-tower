from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.PostList.as_view() , name='List'),
    path(r'^(?P<pk>\d+)$', views.PostDetail.as_view() , name='Detail'),
    path(r'^nuevo$', views.PostCreate.as_view() , name='New'),
    path(r'^editar(?P<pk>\d+)$', views.PostUpdate.as_view() , name='Update'),
    path(r'^borrar(?P<pk>\d+)$', views.PostDelete.as_view() , name='Delete'),
]
