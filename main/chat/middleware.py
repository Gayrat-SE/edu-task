import logging.config


class RequestMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request, response)
        return response


    def process_request(self, request, response):
        user_name = getattr(request.user, 'username', '-')

        if user_name:
            logging.config.dictConfig({
                'version': 1,
                # Version of logging
                'disable_existing_loggers': False,
                'formatters': {

                    'simple': {
                        'format': f'[%(asctime)s] - %(levelname)5s -:%(message)3s -> { user_name }'
                    },

                },
                'handlers': {
                    'file': {
                        'level': 'INFO',
                        'class': 'logging.FileHandler',
                        'filename': 'debug.log',
                        'formatter':'simple'
                    },
                },
                'loggers': {
                'django': {
                        # Add your handlers that have the unbound request filter
                        'handlers': ['file'],
                        'level': 'DEBUG',
                        'propagate': True,
                        # Optionally, add the unbound request filter to your
                        # application.
                    },
                },
            })
    

    



    