from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=100,unique=True)
    id_proof = models.CharField(max_length=12,default=None, unique=True)
    address = models.CharField(max_length=100,default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()                  