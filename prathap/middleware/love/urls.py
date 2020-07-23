from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('sum/', views.get_duration, name='get_duration'),
    path('', views.set_timezone, name='set_timezone'),
    ]
