from django.urls import path, include
from .views import *

app_name='posts'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('like_ajax/', like_ajax, name='like_ajax'),
    path('comment_ajax/', comment_ajax, name='comment_ajax'),
    path('comment_delete/', comment_delete, name='comment_delete'),
]
