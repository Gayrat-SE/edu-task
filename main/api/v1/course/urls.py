from django.urls import path
from .views import CreateHomework

urlpatterns = [
    path('homework/create/', CreateHomework.as_view()),
]