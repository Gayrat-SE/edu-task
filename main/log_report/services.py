from .models import Log
import time
from django.forms.models import model_to_dict
def set_success_log(request, response):
    Log.objects.create(
        username = request.user,
        method = request.method,
        response = response.content.decode(), 
        status = response.status_code,
        duration = time.time() - request.start_time,
        request = request.path,
        headers = str(request.headers),
        url = request.get_full_path()
        )


def set_error_log(request, error):
    Log.objects.create(
        username = request.user,
        method = request.method,
        status = error.status_code,
        error = error,
        duration = time.time() - request.start_time,
        request = request.path,
        url = request.get_full_path(),
        headers = str(request.headers),
        )