from .serializers import (
    CreateHomeworkSerializer,
    SendHomeworkSerializer,
    SubmissionHomeworkList,
    AnswerHomeworkRating
    )
from courses.models import (
    Homework, 
    HomeworkSubmission,
    )
from log_report.api_views import *


class CreateHomework(LogCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = CreateHomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user.teacher)


class SendHomework(LogCreateAPIView):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = SendHomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(student = self.request.user.student, is_answered = True)



class HomeworkSubmissions(LogListAPIView):
    serializer_class = SubmissionHomeworkList
    def get_queryset(self):
        if self.kwargs["pk"]:
            submissions = HomeworkSubmission.objects.filter(homework = self.kwargs["pk"])
            return submissions


class CreateRatingAnswerHomework(LogCreateAPIView):
    serializer_class = AnswerHomeworkRating
    queryset = HomeworkSubmission.objects.all()