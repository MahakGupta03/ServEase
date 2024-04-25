from django.db import models
from Base.models import BaseModel
from django.utils.text import slugify
# Create your models here.
class Services(BaseModel):
    service_name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    service_image = models.ImageField(upload_to='Service')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.service_name)
        super(Services,self).save(*args, **kwargs)
    def __str__(self) -> str:
        return self.service_name