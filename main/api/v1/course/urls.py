from django.urls import path
from .views import CreateHomework, SendHomework, HomeworkSubmissions, CreateRatingAnswerHomework, GetHomeworkArchive, GetAnswerHomeworkArchive

urlpatterns = [
    path('homework/create/', CreateHomework.as_view()),
    path('homework/answer/', SendHomework.as_view()),
    path('submissions/list/<int:pk>/', HomeworkSubmissions.as_view()),
    path('rating/create/', CreateRatingAnswerHomework.as_view()),
    path('homework/archive/', GetHomeworkArchive.as_view()),
    path('answer/archive/', GetAnswerHomeworkArchive.as_view()),
]