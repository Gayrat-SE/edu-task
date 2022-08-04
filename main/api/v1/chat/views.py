from .serializers import ChatSerializersCreate
from chat.models import Message
from rest_framework.generics import CreateAPIView
from main.requestmixins import RequestLogViewMixin

class ChatApi(RequestLogViewMixin, CreateAPIView):
    serializer_class = ChatSerializersCreate
    model = Message

    def perform_create(self, serializer):
        serializer.save(student = self.request.user.student)