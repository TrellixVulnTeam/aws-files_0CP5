from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('now/', views.index, name='index'),
    path('request_id/', views.index, name='index'),
    path('home_page/', views.index1, name='index1'),
]