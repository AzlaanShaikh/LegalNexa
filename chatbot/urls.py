from django.urls import path
from . import views
urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('chatbot/<str:pk>/', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('map', views.map, name='map'),
    
    path('create-chat', views.createChat, name='create-chat'),
    
]