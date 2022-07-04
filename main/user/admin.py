from django.contrib import admin
from .models import Adminstator, Student, StudentGroup, Teacher
# Register your models here.

admin.site.register(Adminstator)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Teacher)