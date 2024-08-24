from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('category/<slug:category_input>/', views.category),
    path('detail/<slug:slug_input>/', views.detail),
    path('', views.index),
]
