from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='Blog-Index'),
    path('blog/entradas/', views.PostList.as_view(), name='Post-List'),
    path('blog/tus-entradas/', views.UserPostList.as_view(), name='UserPost-List'),
    path('blog/buscar/', views.search_posts, name='Search-Post'),
    path('post/detalle/<int:pk>', views.PostDetail.as_view(), name='Post-Detail'),
    path('post/nuevo/', views.PostCreate.as_view(), name='Post-New'),
    path('post/editar/<int:pk>/', views.PostUpdate.as_view(), name='Post-Update'),
    path('post/borrar/<int:pk>', views.PostDelete.as_view(), name='Post-Delete'),
]
