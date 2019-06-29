from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from domain.models import Clinic, Inspection, Patient, Capture
# Register your models here.


class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'director']


admin.site.register(User, UserAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Inspection)
admin.site.register(Patient)
admin.site.register(Capture)
