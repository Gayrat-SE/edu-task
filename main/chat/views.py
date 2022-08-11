from user.models import StudentGroup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import  Message, Room, MessageRoom
from rest_framework.generics import CreateAPIView




class Chat(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Message
    template_name: str = 'chat/room.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentGroup.objects.filter(student = self.request.user.student)[0]
        context['messages'] = Message.objects.filter(group = context['student'])

        return context

class ChatRoom(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Room
    template_name: str = 'chat/roomGroup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Room.objects.filter(id = self.object.id)[0]
        context['messages'] = MessageRoom.objects.filter(room = context['student'])

        return context

class RoomView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Room
    template_name: str = 'chat/rooms.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['group'] = StudentGroup.objects.filter(student=self.request.user.student)[0]
            context['rooms'] = Room.objects.filter(group=context['group'])
        except:
            context['groups'] = StudentGroup.objects.all()
            context['rooms'] = Room.objects.all()

        return context