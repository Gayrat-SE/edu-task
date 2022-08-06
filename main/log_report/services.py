from .models import Log
import json
import time
from django.forms.models import model_to_dict
def set_success_log(request, response):
    resp = response.content
    status = response.status_code
    username = request.user.username
    path = request.path
    duration = time.time() - request.start_time
    method = request.method
    headers = request.headers
    Log.objects.create(
        username = username,
        method = method,
        response = resp.decode(), 
        status = status,
        duration = duration,
        request = path,
        headers = str(headers),
        url = request.get_full_path()
        )


def set_error_log(request, error):
    username = request.user.username
    path = request.path
    duration = time.time() - request.start_time
    method = request.method
    headers = request.headers
    Log.objects.create(
        username = username,
        method = method,
        status = error.status_code,
        error = error,
        duration = duration,
        request = path,
        url = request.get_full_path(),
        headers = str(headers),
        )