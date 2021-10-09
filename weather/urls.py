from django.urls import path
from .import views

urlpatterns = [
    path('weather', views.home, name='weather'),
    path('news', views.news, name='news')
]
