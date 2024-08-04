from django.urls import path
from .views import community_view

urlpatterns = [
    path('', community_view, name='community'),
]
