from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tourist_attractions, name='index'),
]

