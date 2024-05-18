from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import FileField
from .managers import CustomUserManager
from Base.models import BaseModel
from Services.models import Services
# Create your models here.

class CustomUser(BaseModel,AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=100)
    dob = models.DateField()
    description = models.CharField(max_length=500, default=None)
    id_proof_type = models.CharField(max_length=50,default=None)
    id_proof_number = models.CharField(max_length=12,default=None)
    address = models.CharField(max_length=100,default=None)
    state = models.CharField(max_length=100,default=None)
    city = models.CharField(max_length=100,default=None)
    district = models.CharField(max_length=100,default=None)
    is_customer = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    # profile_image = models.ImageField(upload_to='media/Profile/')
    profile_image = models.FileField(upload_to='assets/Profile')
    service_type = models.OneToOneField(Services, on_delete = models.DO_NOTHING, related_name='user', blank=True, null = True)
    service_name = models.CharField(max_length=100,  default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()    

    
