from .serializers import *
from rest_framework import generics
from user.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from main.generation_pdf import pdf_file_mark
from rest_framework.validators import ValidationError


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]
    

class StudentUpdate(generics.UpdateAPIView):
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

class AdminUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer


class FileRatings(APIView):
    

    def get(self, request):
        file = Student.objects.filter(id = request.user.student.id)[0]
        if file.file_ratings:
            serializer = FileRatingSerializers(file)
            pdf_file_mark(request, file)
            return Response(serializer.data)
        
        raise ValidationError({"msg":"no data"})

        