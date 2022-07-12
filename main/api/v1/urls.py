from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('course/', include('api.v1.course.urls')),
    ]