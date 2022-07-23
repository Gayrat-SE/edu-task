from urllib import request
from lesson.models import Event
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer
)
from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import  IsAuthenticated

class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =CreateEventSerializer
    queryset = Event.objects.all()




class ListLesson(ListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        teacher_lesson = Event.objects.filter(teacher_id = self.request.user.teacher.id,
            start_date__gte = self.request.GET.get('start_date'), end_date__lte = self.request.GET.get('end_date'))
        return teacher_lesson