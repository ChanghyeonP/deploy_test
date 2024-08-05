from django.urls import path
from .views import community_view, delete_post

urlpatterns = [
    path('', community_view, name='community'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
