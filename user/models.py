from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 
    username = models.CharField(unique=True, max_length=150)  
    image=models.ImageField(upload_to='users/images', blank=True,null=True)
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username