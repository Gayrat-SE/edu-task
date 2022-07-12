from .serializers import CreateHomeworkSerializer, SendHomeworkSerializer
from rest_framework.generics import CreateAPIView
from courses.models import Homework, HomeworkSubmission
from rest_framework.views import APIView
from rest_framework.response import Response
class CreateHomework(CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = CreateHomeworkSerializer


class SendHomework(CreateAPIView):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = SendHomeworkSerializer