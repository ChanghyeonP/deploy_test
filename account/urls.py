from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  # 회원가입 뷰 추가
   #path('logout/', views.logout_view, name='logout'),  # 로그아웃 뷰 추가
]
