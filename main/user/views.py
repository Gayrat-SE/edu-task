from django.shortcuts import render
from .models import *
# Create your views here.


def dashboard(request):
    return render(request, 'users/admin/index.html')


def studentGroup(request):
    return render(request, 'users/student/studentGroup_list.html')

def studentList(request):
    student = Student.objects.all()
    context = {
        'student':student
    }
    return render(request, 'users/student/student_list.html', context)