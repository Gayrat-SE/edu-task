from django.shortcuts import render, redirect
from .models import *
from courses.models import Homework
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
# Create your views here.

class Login(LoginView):
    template_name: str = "users/login_simple.html"
    def get_success_url(self):
        success_url = reverse_lazy("index")
        return success_url



def dashboard(request):
    return render(request, 'index.html')


def studentGroup(request):
    groups = StudentGroup.objects.all()
    print(request.user.owner)
    context = {
        'groups':groups
    }
    return render(request, 'users/student/studentGroup_list.html', context)

def studentList(request, pk):
    student = StudentGroup.objects.filter(id = pk)
    context = {
        'student':student,
        'pk':pk,
    }
    return render(request, 'users/student/student_list.html', context)