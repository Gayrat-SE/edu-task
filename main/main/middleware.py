import logging
import time
from django.utils.deprecation import MiddlewareMixin
import socket


logger = logging.getLogger('django')

class RequestMiddleware(MiddlewareMixin):



    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):

        if response['content-type'] == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'
        log_data = {
            'user': request.user.username,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),

            'response_status': response.status_code,
            'response_body': response_body,

            'run_time': time.time() - request.start_time,
        }
        logger.info(log_data)
        return response