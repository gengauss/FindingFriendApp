# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='chat'),
    path(r'<str:channel_link>/', views.room, name='room')
]
