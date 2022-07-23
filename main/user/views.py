from multiprocessing import context
from lesson.models import Event
from django.shortcuts import render
from courses.models import Homework, HomeworkSubmission
from .models import *
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from lesson.models import Event
# Create your views here.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class TeacherProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "user"
    model = User
    template_name: str = "users/teacher/teacherProfile.html"

class StudentProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "user"
    model = User
    template_name: str = "users/student/studentProfile.html"

class AdminProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    model = User
    template_name: str = "users/admin/adminProfile.html"



class Dashboard(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        student_count = Student.objects.all().count()
        teacher_count = Teacher.objects.all().count()
        try:
            user_count = User.objects.all().count()
            answer = HomeworkSubmission.objects.filter(student = request.user.student.id).count()
            homework = Homework.objects.filter(student_group__student = request.user.student.id).count()
            context = {
                "answer":answer,
                "homework":homework,
                "student_count":student_count,
                "teacher_count":teacher_count,
                "user_count":user_count,
            }
            return render(request, 'index.html', context=context)
        except ObjectDoesNotExist:
            user_count = User.objects.all().count()
            group = StudentGroup.objects.all()
            context = {
                "student_count":student_count,
                "teacher_count":teacher_count,
                "user_count":user_count,
                'groups':group
            }
            return render(request, 'index.html', context=context)


class Groups(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "groups"
    model = StudentGroup
    template_name: str = 'users/student/studentGroup_list.html'
        

class DetailGroup(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/student/studentList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentGroup.objects.filter(id=self.object.id)
        return context

class TeacherList(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Teacher
    template_name: str = 'users/teacher/teacherList.html'
    context_object_name = "teachers"


class StudentGroups(LoginRequiredMixin, ListView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/student/groups.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['groups'] = StudentGroup.objects.filter(student = self.request.user.student.id)
            context['homeworks'] = Homework.objects.filter(student_group__in = context['groups'])
            return context
        except ObjectDoesNotExist:
            return {"msg":"error"}


class GetStudentMark(LoginRequiredMixin, ListView):
    login_url = "login"
    model = HomeworkSubmission
    template_name: str = 'users/student/studentMarks.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['ratings'] = HomeworkSubmission.objects.filter(student = self.request.user.student)
        except ObjectDoesNotExist:
            return {"error":"you dont have permission"}
        return context


class StudentCalendar(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Event
    template_name: str = 'users/student/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context = super().get_context_data(**kwargs)
            context['student'] = StudentGroup.objects.filter(student = self.request.user.student.id)
            context['lesson'] = Event.objects.filter(groups__in = context['student'] )
            print(context["lesson"])
        except ObjectDoesNotExist:
            return {"error":"you dont have permission"}
        return context

class TeacherCalendar(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Event
    template_name: str = 'users/teacher/calendar.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['groups'] = StudentGroup.objects.all()
        return context