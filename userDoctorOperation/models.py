
from django.db import models
from django.contrib.auth import get_user_model 
from base.models import DentalService
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialties = models.ManyToManyField(DentalService, related_name='specialties')

    def __str__(self):
        return self.user.username

class Slot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    isBooked = models.BooleanField(default=False)
    patient = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Slot for {self.doctor} on {self.date} from {self.startTime} to {self.endTime}"

    def clean(self):
    
        start_datetime = datetime.combine(self.date, self.startTime)
        end_datetime = datetime.combine(self.date, self.endTime)
        duration = end_datetime - start_datetime

        if duration < timedelta(hours=1):
            raise ValidationError("Slot duration must be at least one hour.")
    
PAYMENT_METHOD_CHOICES = (
    ('cash', 'Cash'),
    ('card', 'Card'),
)

class Payment(models.Model):
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash')
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Slot: {self.slot} ({self.amount} {self.get_paymentMethod_display()})"