from django.urls import path
from .views import *
urlpatterns = [
    path('create/lesson/', CreateEvent.as_view()),
    path('list/lesson/teacher/', ListLessonTeacher.as_view()),
    path('list/lesson/student/', ListLessonStudent.as_view()),
    path('update/lesson/<int:pk>/', UpdateEvent.as_view()),
]