from django.db import models
from user.models import CustomUser
from base.models import DentalService
# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialties = models.ManyToManyField(DentalService, related_name='specialties')
   

    def __str__(self):
        return self.user.username
    
class Slot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    isBooked = models.BooleanField(default=False)
    patient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"Slot for {self.doctor} on {self.date} from {self.startTime} to {self.endTime}"