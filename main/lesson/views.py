from user.models import *
from courses.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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