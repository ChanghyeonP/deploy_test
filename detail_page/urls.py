from django.urls import path
from .views import tourist_attraction_detail, delete_comment

urlpatterns = [
    path('<int:content_id>/', tourist_attraction_detail, name='tourist_attraction_detail'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]
