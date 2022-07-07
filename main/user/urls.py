from django.urls import path
from .views import *
urlpatterns = [
    path('dashboards', dashboard, name='index'),
    path('student-groups', studentGroup, name='student-group'),
    path('student-list/<int:pk>', studentList, name='students')
]