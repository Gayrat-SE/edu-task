from django.contrib import admin
from .models import Admin, Student, StudentGroup, Teacher, User, StudentBulkUpload
# Register your models here.

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Teacher)
admin.site.register(User)

admin.site.register(StudentBulkUpload)