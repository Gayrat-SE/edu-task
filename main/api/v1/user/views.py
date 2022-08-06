from .serializers import *
from rest_framework import generics
from user.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from log_report.api_views import LogCreateAPIView, LogRetrieveUpdateDestroyAPIView, LogDestroyAPIView, LogUpdateAPIView


class StudentCreate(LogCreateAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]
    

class StudentUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer




class StudentGroupCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAuthenticated]



class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentGroupDetailList(generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer

class AdminCreate(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]

class AdminUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer


class UserDelete(LogDestroyAPIView, generics.DestroyAPIView):
    queryset = User
    permission_classes = [IsAdminUser]


class StudentGroupDelete(generics.DestroyAPIView):
    queryset = StudentGroup
    permission_classes = [IsAdminUser]