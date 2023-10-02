from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Consultation
from base.models import DentalService
class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['name', 'email', 'mobile_number', 'doctor_name', 'preferred_time', 'preferred_date']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'mobile_number': forms.TextInput(attrs={'required': True}),
            'doctor_name': forms.TextInput(attrs={'required': True}),
            'preferred_time': forms.TimeInput(attrs={'required': True}),
            'preferred_date': forms.DateInput(attrs={'required': True}),
        }

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data.get('preferred_date')
        if preferred_date:
            today = datetime.now().date()
            if preferred_date <= today:
                raise ValidationError("Preferred date cannot be yesterday or earlier.")
        return preferred_date

    def clean_preferred_time(self):
        preferred_time = self.cleaned_data.get('preferred_time')
        if preferred_time:
            start_time = datetime.strptime('09:00:00', '%H:%M:%S').time()
            end_time = datetime.strptime('17:00:00', '%H:%M:%S').time()
            if not start_time <= preferred_time <= end_time:
                raise ValidationError("Preferred time must be between 9:00 AM and 5:00 PM.")
        return preferred_time



