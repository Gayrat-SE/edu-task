from django.urls import path
from .views import ListArchivePost


urlpatterns = [
    path('list/', ListArchivePost.as_view(), name='log')

]