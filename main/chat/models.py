from django.db import models
from user.models import StudentGroup, Teacher, Student, User, Admin
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Admin, on_delete=models.CASCADE)
    group = models.ManyToManyField(StudentGroup, blank=True, related_name='group')

class MessageRoom(models.Model):
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ('date_added',)

class Message(models.Model):
    group = models.ForeignKey(StudentGroup, related_name='messages', on_delete=models.PROTECT, blank=True, null=True)
    content = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)