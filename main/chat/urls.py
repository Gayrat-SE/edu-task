from django.urls import path
from .views import Chat, ChatRoom, RoomView

urlpatterns = [

    path('group/', Chat.as_view(), name='room'),
    path('rooms/', RoomView.as_view(), name='rooms'),
    path('<int:pk>/', ChatRoom.as_view(), name='roomGroup'),
]