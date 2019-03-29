from django.db import models
from django.conf import settings

# Create your models here.
class Clinics(models.Model):
    name = models.CharField(max_length=255)
    contact_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    BIK  = models.CharField(max_length=45)
    INN = models.CharField(max_length=45)

class Doctors(models.Model):
    clinic_id = models.ForeignKey(
        'Clinics',
        on_delete = models.CASCADE
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    surname = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45, null = True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

class Patients(models.Model):
    clinic_id = models.ForeignKey(
        'Clinics',
        on_delete = models.CASCADE
    )
    doctor_id = models.ForeignKey(
        'Doctors',
        on_delete = models.CASCADE,
        null = True
    )
    card_number = models.CharField(max_length=45)

class Inspections(models.Model):
    patient_id = models.ForeignKey(
        'Patients',
        on_delete = models.CASCADE
    )
    inspection_date = models.DateTimeField()
    code = models.IntegerField(unique=True)

class Captures(models.Model):
    inspection_code = models.ForeignKey(
        'Inspections',
        to_field='code',
        on_delete = models.CASCADE
    )
    storage_key = models.CharField(max_length=45)