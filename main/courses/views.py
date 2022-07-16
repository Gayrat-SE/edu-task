from django.shortcuts import render
from user.models import StudentGroup
from .models import Homework, HomeworkSubmission
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DetailHomework(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = "hometasks/task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_id'] = StudentGroup.objects.get(id = self.object.id)
        context['homework'] = Homework.objects.filter(student_group = self.object.id)
        return context

def sendhomework(request):
    list_groups = StudentGroup.objects.all()
    context = {'list_groups':list_groups}
    return render(request, 'hometasks/hometask.html', context)