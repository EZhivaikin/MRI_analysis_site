from django.urls import path, re_path
from . import views

urlpatterns = [
    path('clinic_create_edit/', views.clinics_create_edit,
         name='clinic-create-edit'),
    path('doctors_list/', views.DoctorListView.as_view(),
         name='doctors-list'),
    path('doctor_create_edit/<int:doctor_id>', views.DoctorCreateEdit.as_view(),
         name='doctor-create-edit'),
]
