from django.shortcuts import render
from .models import Log
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListArchivePost(LoginRequiredMixin, generic.ListView):
    login_url = "login"
    model = Log
    template_name: str = 'users/archives.html'