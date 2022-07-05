from django.urls import path
from .views import *
urlpatterns = [
    path('dashboards', dashboard),
    path('student-groups', studentGroup)
]