from django.urls import path
from .views import *
urlpatterns = [
    path('create/lesson/', CreateEvent.as_view()),
    path('list/lesson/', ListLesson.as_view())
]