from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from domain.models import Clinic, Inspection, Patient, Capture
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Clinic)
admin.site.register(Inspection)
admin.site.register(Patient)
admin.site.register(Capture)

