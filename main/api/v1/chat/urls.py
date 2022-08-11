from django.urls import path

from .views import ChatApi, RoomApi, ChatRoomApi

urlpatterns = [
    path('create/', ChatApi.as_view()),
    path('message/create/', ChatRoomApi.as_view()),
    path('group/create/', RoomApi.as_view()),
]