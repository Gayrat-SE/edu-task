from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from user.models import *
from rest_framework.response import Response
from rest_framework import status

class StudentCreate(APIView):
    
    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            group_id = self.request.POST.get('group')
            studentGroup = StudentGroup.objects.filter(id=group_id)[0]
            username = serializer.data['username']
            student = Student.objects.filter(user__username = username)[0]
            studentGroup.student.add(student.id)
            studentGroup.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentGroupCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer