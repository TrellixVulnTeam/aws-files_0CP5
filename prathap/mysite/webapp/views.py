from django.shortcuts import render

from django.http import HttpResponse
import datetime
import uuid

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(str(datetime.datetime.now()))
    return HttpResponse(str(uuid.uuid4()))
    
def index1(request):
    
    return HttpResponse('''
    <!doctype html>
    <html>
    <body>
    
    <h2> List 1</h2>
    
    <ul>
    <li> Team 1 </li>
    <li> Team 2 </li>
    <li> Team 3 </li>
    </ul>
    </body>
    </html>
    
    ''')