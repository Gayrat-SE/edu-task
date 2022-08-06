from .serializers import *
from user.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from log_report.api_views import *


class StudentCreate(LogCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]
    

class StudentUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer




class StudentGroupCreate(LogCreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAuthenticated]



class TeacherCreate(LogCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(LogListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(LogListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentGroupDetailList(LogRetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer

class AdminCreate(LogCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]

class AdminUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer


class UserDelete(LogDestroyAPIView):
    queryset = User
    permission_classes = [IsAdminUser]


class StudentGroupDelete(LogDestroyAPIView):
    queryset = StudentGroup
    permission_classes = [IsAdminUser]