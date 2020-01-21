# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/c/(?P<channel_link>[^/]+)/$', consumers.ChatConsumer),
]
