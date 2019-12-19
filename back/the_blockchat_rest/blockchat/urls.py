from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('messages/', views.messages, name='messages'),
    path('channels/', views.channels, name='channels'),
    path('chatrooms/', views.chatrooms, name='chatrooms'),
    path('users/', views.users, name='users'),
    # path('messages/<str:channel>', views.messages, name='messages'),
]
