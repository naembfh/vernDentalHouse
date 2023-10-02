from django.db import models

# Create your models here.
class DentalService(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='services/images')

    def __str__(self):
        return self.name
    
    
class Consultation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    doctor_name = models.CharField(max_length=255)
    preferred_time = models.TimeField()
    preferred_date = models.DateField()
    isConsultate =models.BooleanField(default=False)

    def __str__(self):
        return self.name