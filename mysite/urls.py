
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('daftar/', views.daftar),
    path('blog/', include('blog.urls')),
    path('kontak/', include('contact.urls')),
    path('admin/', admin.site.urls),
]
