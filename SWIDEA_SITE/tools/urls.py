from django.urls import path
from .views import *

app_name='tools'
urlpatterns = [
    path('', tool, name='tool'),
    path('<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]