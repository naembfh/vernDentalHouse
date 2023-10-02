from django import forms
from userDoctorOperation.models import Slot, Doctor,Payment
from base.models import DentalService
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['date', 'startTime', 'endTime', 'doctor']



class AddDoctorForm(forms.Form):
    specialties = forms.ModelMultipleChoiceField(
        queryset=DentalService.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
   
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialties'].label = f"Select Specialties for Dr. {user.username}"
        
        
class PaymentForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Payment Amount')

    class Meta:
        model = Payment
        fields = ['paymentMethod',  'amount']