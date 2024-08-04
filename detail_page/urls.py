from django.urls import path
from .views import tourist_attraction_detail

urlpatterns = [
    path('<int:content_id>/', tourist_attraction_detail, name='tourist_attraction_detail'),
]
