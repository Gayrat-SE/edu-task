from django.urls import path
from .views import *
urlpatterns = [
    path('student-create', StudentCreate.as_view()),
    path('group-create', StudentGroupCreate.as_view()),
    path('teacher-create', TeacherCreate.as_view()),
    ]