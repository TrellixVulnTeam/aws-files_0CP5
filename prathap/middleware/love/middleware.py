"""import time


class TimeDurationMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        start = time.time()
        print("Current Time =", start)
        response = self.get_response(request)
        end = time.time()
        print("end Time =", end)
        duration = end-start
        print("function_duration: ",duration)
        return response

    def process_exception(self, request, exception):
        print (exception.message)
        return None
"""



import pytz

from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()"""
        return self.get_response(request)