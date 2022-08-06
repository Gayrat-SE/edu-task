from lesson.models import Event
from user.models import StudentGroup
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer,
    UpdateEventSerializer
)
from rest_framework.permissions import  IsAuthenticated
from log_report.api_views import *


class CreateEvent(LogCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =CreateEventSerializer
    queryset = Event.objects.all()


class UpdateEvent(LogUpdateAPIView):
    serializer_class = UpdateEventSerializer
    queryset = Event.objects.all()



class ListLessonTeacher(LogListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        teacher_lesson = Event.objects.filter(teacher_id = self.request.user.teacher.id,
            start_date__gte = self.request.GET.get('start_date'), end_date__lte = self.request.GET.get('end_date'))
        return teacher_lesson

class ListLessonStudent(LogListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        group = StudentGroup.objects.filter(student = self.request.user.student)[0]
        student_lesson = Event.objects.filter(groups = group,
            start_date__gte = self.request.GET.get('start_date'), end_date__lte = self.request.GET.get('end_date'))
        return student_lesson