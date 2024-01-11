from django.urls import path, include
from .views import *
urlpatterns = [
    path('', posts_list),
    path('<int:pk>', posts_read),
    path('create', posts_create),
    path('<int:pk>/update', posts_update),
    path('<int:pk>/delete', posts_delete),
    path('<int:post_id>/comments/create', comments_create),
    # path('create_final', posts_create_final),
]