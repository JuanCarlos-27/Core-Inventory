from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(('Correo electronico'), unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    dni = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=60)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
