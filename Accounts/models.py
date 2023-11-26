from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import FileField
from .managers import CustomUserManager
from Base.models import BaseModel
# Create your models here.

class CustomUser(BaseModel,AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=100,unique=True)
    id_proof = models.CharField(max_length=12,default=None, unique=True)
    address = models.CharField(max_length=100,default=None)
    is_customer = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    # profile_image = models.ImageField(upload_to='assets/Profile')
    profile_image = models.FileField(upload_to='assets/Profile')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()                  