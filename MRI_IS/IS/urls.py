from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.home, name='IS-home'),
    path(r'about/', views.about, name='IS-about'),
]