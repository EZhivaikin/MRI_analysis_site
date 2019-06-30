from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'))
    patronymic = models.CharField('Отчество', max_length=255, blank=True)
    phone = models.CharField("Телефон", max_length=12)
    clinic_id = models.IntegerField(blank=True)
