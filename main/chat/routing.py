from django.urls import path

from .consumers import ChatStudent, ChatRoom

websocket_urlpatterns = [
    path('ws/chat/<int:room_name>/', ChatStudent.as_asgi()),
    path('group/chat/<int:room_name>/', ChatRoom.as_asgi()),
]