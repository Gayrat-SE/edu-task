from django.urls import path
from .views import ListArchivePost


urlpatterns = [
    path('archive/', ListArchivePost.as_view(), name='archive')

]