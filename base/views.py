from django.shortcuts import render,redirect
from .models import DentalService,Consultation
from userDoctorOperation.models import Slot
from .forms import ConsultationForm
from django.contrib import messages
# Create your views here.
def home(request):
    dentalServices = DentalService.objects.all()
    print(dentalServices)
    consultaion = Consultation.objects.all()
    print(consultaion)

    if request.method == 'POST':
        print('hlw')
        form = ConsultationForm(request.POST)
        if form.is_valid():
            print('here')
            data = form.cleaned_data['email']  
            print(data)
            form.save()
            messages.success(request, 'Successfully added for consulation.')
            return redirect('home') 
        else:
            print('not valid')
            print(form.errors)
    else:
        form = ConsultationForm()
    context = {'dentalServices': dentalServices, 'form': form}
    return render(request, 'base/base.html', context)

