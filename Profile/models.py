from django.db import models

# Create your models here.

class Profile(models.Model):
    isUser = models.BooleanField(default=True)
