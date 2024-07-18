from django.urls import path
from . import views

urlpatterns = [
    path('<int:content_id>/', views.tourist_attraction_detail, name='detail'),
]
