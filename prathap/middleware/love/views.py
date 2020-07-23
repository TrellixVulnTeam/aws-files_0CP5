from django.shortcuts import render
from django.http import HttpResponse
import pytz
# Create your views here.

"""
def index(request):
    return HttpResponse('Hai Prathap')


def get_duration(request):

    a=2
    b=3+4%6
    c=4*6^2
    sum = a+b+c
    return HttpResponse(sum)
"""

from django.shortcuts import redirect, render

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})
