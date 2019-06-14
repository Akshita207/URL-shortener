
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shortener.views import HomeView, URLRedirectView, CustomURLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customurl/', CustomURLView.as_view(), name='customurl'),
    path('', HomeView.as_view()),
    path('<slug:shortcode>/', URLRedirectView.as_view(), name='scode'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)