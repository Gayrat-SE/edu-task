import time
from django.utils.deprecation import MiddlewareMixin
from log_report.services import set_success_log, set_error_log
from user.models import User
from django.utils.timezone import now

class RequestMiddleware(MiddlewareMixin):



    def process_request(self, request):
        request.start_time = time.time()

        try:
            
            if request.user.is_authenticated:
                User.objects.filter(pk=request.user.pk).update(last_activity=now())
        except:
            pass
        

    def process_response(self, request, response):
        return response
