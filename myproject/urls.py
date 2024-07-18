from django.contrib import admin
from django.urls import path, include
from account import views as account_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.login_view, name='login'),  # 메인 페이지로 로그인 뷰 설정
    path('account/', include('account.urls')),
    path('myapp/', include('myapp.urls')),  # 로그인 후 이동할 페이지
    path('', include('detail_page.urls')),
]
