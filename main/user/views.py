from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.


def dashboard(request):
    return render(request, 'index.html')


def studentGroup(request):
    groups = StudentGroup.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'users/student/studentGroup_list.html', context)

def studentList(request, pk):
    student = StudentGroup.objects.filter(id = pk)
    context = {
        'student':student,
        'pk':pk
    }
    return render(request, 'users/student/student_list.html', context)