from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='Blog-Index'),
    path('entradas/', views.PostList.as_view(), name='Post-List'),
    path('detalle/', views.PostDetail.as_view(), name='Post-Detail'),
    path('nuevo/', views.PostCreate.as_view(), name='Post-New'),
    path('editar/<int:pk>/', views.PostUpdate.as_view(), name='Post-Update'),
    path('borrar/<int:pk>', views.PostDelete.as_view(), name='Post-Delete'),
]
