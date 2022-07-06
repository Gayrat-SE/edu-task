from django.urls import path
from .views import *
urlpatterns = [
    path('dashboards', dashboard),
    path('student-groups', studentGroup),
    path('student-list/<int:pk>', studentList, name='students')
]