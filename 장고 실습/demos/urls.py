from django.urls import path
from .views import index, cal

app_name = 'demos'

urlpatterns = [
    path("index/", index, name='index'),
    path("cal/", cal),
]