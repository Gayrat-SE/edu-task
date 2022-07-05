from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'users/admin/index.html')


def studentGroup(request):
    return render(request, 'users/student/studentGroup_list.html')