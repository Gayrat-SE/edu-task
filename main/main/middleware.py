import time
from django.utils.deprecation import MiddlewareMixin
from log_report.services import set_success_log, set_error_log



class RequestMiddleware(MiddlewareMixin):



    def process_request(self, request):
        request.start_time = time.time()
        

    def process_response(self, request, response):
        return response
