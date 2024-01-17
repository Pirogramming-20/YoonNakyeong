from django.urls import path
from .views import *

app_name='ideas'
urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('<int:idea_id>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]