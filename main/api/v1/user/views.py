from .serializers import *
from user.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from log_report.api_views import *
from .permissions import IsAdminOrReadOnly, IsStudent, IsTeacher
from django.http import JsonResponse


class StudentBulk(LogCreateAPIView):
    queryset = StudentBulkUpload
    serializer_class = StudentBulkCreateSerializers
    permission_classes = [IsAdminUser]

class StudentCreate(LogCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAdminOrReadOnly]
    

class StudentUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer




class StudentGroupCreate(LogCreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAdminOrReadOnly]



class TeacherCreate(LogCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class TeacherUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(LogListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(LogListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentGroupDetailList(LogRetrieveUpdateDestroyAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer
    def patch(self, request, *args, **kwargs):
        group = StudentGroup.objects.filter(id=self.kwargs.get("pk"))
        for students in group:
            students.student.add(self.request.POST['student'])
        return JsonResponse({"group":"access"})

class AdminCreate(LogCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAdminOrReadOnly]

class AdminUpdate(LogRetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer


class UserDelete(LogDestroyAPIView):
    queryset = User
    permission_classes = [IsAdminUser]


class StudentGroupDelete(LogDestroyAPIView):
    queryset = StudentGroup
    permission_classes = [IsAdminUser]