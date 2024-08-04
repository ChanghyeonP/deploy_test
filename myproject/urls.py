from django.contrib import admin
from django.urls import path, include
from account import views as account_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.login_view, name='login'),  # 메인 페이지로 로그인 뷰 설정
    path('account/', include('account.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('community/', include('community.urls')),
    path('myapp/', include('myapp.urls')),  # 로그인 후 이동할 페이지
    path('', include('detail_page.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)