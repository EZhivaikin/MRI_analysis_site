from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create_edit/', views.clinics_create_edit, name='Clinic-create-edit'),
]