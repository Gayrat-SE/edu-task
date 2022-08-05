from .models import Log
import json
import time

def set_success_log(request, response):

    resp = response.content.decode()
    print(time.time())

    Log.objects.create(response = str(response.content.decode('utf-8')) )


def set_error_log(request, error):
    print(error)
