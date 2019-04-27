from django.db import models
from django.conf import settings
from users.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    contact_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    BIK = models.CharField(max_length=45)
    INN = models.CharField(max_length=45)


class Doctor(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)


class Patient(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True
    )
    card_number = models.CharField(max_length=45)


class Inspections(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    inspection_date = models.DateTimeField()
    code = models.IntegerField(unique=True)


class Captures(models.Model):
    inspection_code = models.ForeignKey(
        'Inspections',
        to_field='code',
        on_delete=models.CASCADE
    )
    storage_key = models.CharField(max_length=45)
