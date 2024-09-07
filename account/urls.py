from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.register_users, name='register'),
]
