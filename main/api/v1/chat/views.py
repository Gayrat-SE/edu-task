from log_report.api_views import LogCreateAPIView
from .serializers import ChatSerializersCreate
from chat.models import Message


class ChatApi(LogCreateAPIView):
    serializer_class = ChatSerializersCreate
    model = Message

    def perform_create(self, serializer):
        serializer.save(student = self.request.user.student)