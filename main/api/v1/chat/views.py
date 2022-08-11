from log_report.api_views import LogCreateAPIView
from .serializers import ChatSerializersCreate, ChatMessageSerializers, RoomSerializersCreate
from chat.models import Message, MessageRoom, Room


class ChatApi(LogCreateAPIView):
    serializer_class = ChatSerializersCreate
    model = Message

    def perform_create(self, serializer):
        serializer.save(student = self.request.user.student)


class ChatRoomApi(LogCreateAPIView):
    serializer_class = ChatMessageSerializers
    model = MessageRoom

class RoomApi(LogCreateAPIView):
    serializer_class = RoomSerializersCreate
    model = Room