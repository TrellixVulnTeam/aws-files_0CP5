from django.urls import path
from .views import get_all_users, user_posts, get_post_details

urlpatterns = [
    path('all/', get_all_users),
    path('post/', user_posts),
    path('post/details/', get_post_details),
    ]