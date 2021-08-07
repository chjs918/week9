from django.urls import path
from . import views

urlpatterns = [
    path('messageList/', views.messageList, name='messageList'),
    path('newMessage/', views.newMessage, name='newMessage'),
    path('sendMessage/', views.sendMessage, name='sendMessage'),
]