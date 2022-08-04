from .serializers import *
from rest_framework import generics
from user.models import *
from rest_framework.permissions import IsAuthenticated
from main.requestmixins import RequestLogViewMixin


class StudentCreate(RequestLogViewMixin, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]
    

class StudentUpdate(RequestLogViewMixin, generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer




class StudentGroupCreate(RequestLogViewMixin, generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAuthenticated]



class TeacherCreate(RequestLogViewMixin, generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdate(RequestLogViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(RequestLogViewMixin, generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(RequestLogViewMixin, generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentGroupDetailList(RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer

class AdminCreate(RequestLogViewMixin, generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]

class AdminUpdate(RequestLogViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer



        