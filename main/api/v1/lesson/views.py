from django.shortcuts import render
from lesson.models import Event
from user.models import StudentGroup
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer
)
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import status
from  rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import json
import requests


class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =CreateEventSerializer
    queryset = Event.objects.all()




class ListLesson(ListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        teacher_lesson = Event.objects.filter(teacher_id = self.request.user.teacher.id)
        return teacher_lesson