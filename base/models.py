from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Medicine Model...
class Medicine(models.Model):
    product_image = models.ImageField(upload_to='productimages/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacture_date = models.DateField(editable=True)    
    expiry_date = models.DateField(editable=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)    

    def __str__(self):
        return self.name
    
    