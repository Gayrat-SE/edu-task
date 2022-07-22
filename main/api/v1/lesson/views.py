from django.shortcuts import render
from lesson.models import Event
from user.models import StudentGroup
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer
)
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from  rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import json
import requests


class CreateEvent(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class =CreateEventSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            id= serializer.data.get('groups')
            students = StudentGroup.objects.filter(id=id)
            students = students[0]
            data = requests.post("https://api.zoom.us/v2/users/me/meetings", headers={
                'content-type': "application/json",
                "Authorization": f"Bearer {request.session['zoom_access_token']}"
                }, json={
                "topic": f"Interview with { students.name }",
                "type": 2,
                "start_time": start_date,
                "duration": 90,
                "timezone": "Asia/Tashkent"
            })
            event = Event(title=title, start_date=start_date, end_date=end_date, groups=students, zoom_start_url=data.json()["start_url"],
            zoom_join_url =data.json()["join_url"], teacher_id = request.user.teacher.id)
            event.save()
            return Response(CreateEventSerializer(event).data, status=status.HTTP_201_CREATED)

        return Response({"msg":"No Content"}, status=status.HTTP_204_NO_CONTENT)



class ListLesson(ListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        teacher_lesson = Event.objects.filter(teacher_id = self.request.user.teacher.id)
        return teacher_lesson