from django.shortcuts import render
from user.models import StudentGroup
from .models import Homework
# Create your views here.


def student_groups(request):
    student_groups = StudentGroup.objects.filter(student = request.user.student.id)


def homeworklist(request, pk):
    homeworks = Homework.objects.filter(student_group = pk)