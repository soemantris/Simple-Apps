
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('daftar/', views.daftar),
    path('blog/', include('blog.urls')),
    path('kontak/', include('contact.urls')),
    path('accounts/', include('account.urls', namespace='account')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
