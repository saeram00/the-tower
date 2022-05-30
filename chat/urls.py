from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.MessageList.as_view(), name='Inbox'),
    path('buscar-mensajes/', views.search_messages, name='Search-Chat'),
    path('mensaje/detalle/<int:pk>', views.MessageDetail.as_view(), name='Chat-Detail'),
    path('mensaje/nuevo/', views.MessageCreate.as_view(), name='New-Message'),
    path('mensaje/editar/<int:pk>', views.MessageUpdate.as_view(), name='Edit-Message'),
    path('mensaje/borrar/<int:pk>', views.MessageDelete.as_view(), name='Del-Message'),
]
