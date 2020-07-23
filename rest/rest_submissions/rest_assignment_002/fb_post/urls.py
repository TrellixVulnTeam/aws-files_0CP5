from django.urls import path
from .views import (
    create_post,
    get_post,
    reply_to_comment,
    react_to_post,
    react_to_comment,
    delete_post,
    create_comment
)

urlpatterns = [
    path('post/', create_post),
    path('post/<int:post_id>/', get_post),
    path('comment/<int:comment_id>/reply/create/', reply_to_comment),
    path('post/<int:post_id>/react/', react_to_post),
    path('comment/<int:comment_id>/react/', react_to_comment),
    path('post/<int:post_id>/delete/', delete_post),
    path('post/<int:post_id>/comment/create/', create_comment),
    ]

