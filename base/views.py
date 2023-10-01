from django.shortcuts import render
from .models import DentalService
# Create your views here.
def home(request):
    dentalServices=DentalService.objects.all()
    # for service in dentalServices:
    #     print(service.id)
    # print(dentalServices)
    context={'dentalServices':dentalServices}
    return render(request,'base/base.html',context)

def dashboard(request):
    return render(request,'base/dashboard.html')
