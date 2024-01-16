import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = CountryField(verbose_name='страна',
                           **NULLABLE)  # installed package django-countries with pyuca translation
    token = models.CharField(max_length=100, default=uuid.uuid4)
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован')

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'check_verification',
                'Can check email verification of account'
            )
        ]
