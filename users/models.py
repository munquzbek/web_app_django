from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from catalog.models import NULLABLE


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = CountryField(verbose_name='страна')  # installed package django-countries with pyuca translation

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []
