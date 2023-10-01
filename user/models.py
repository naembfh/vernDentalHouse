# user/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userTypeChoices = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('normal', 'Normal User'),  # Default choice
    ]
    userType = models.CharField(max_length=10, choices=userTypeChoices, default='normal')
    userImage = models.ImageField(upload_to='userImages/', blank=True, null=True)

    def __str__(self):
        return self.user.username


