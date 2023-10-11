from django.shortcuts import render,get_object_or_404
from userDoctorOperation.models import Slot
from django.shortcuts import render, redirect
from userDoctorOperation.models import Slot,Doctor,Payment
from .forms import SlotForm ,AddDoctorForm,PaymentForm
from django.contrib.auth.models import User
from base.models import Consultation
from django.utils import timezone
from django.db.models import F, ExpressionWrapper, fields,Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

# user action

def userDoctorAppointment(request):
    user = request.user
    appointments = Slot.objects.filter(isBooked=True)

    if user.userprofile.userType == 'doctor':
        appointments = appointments.filter(doctor=user.doctor)
    elif user.userprofile.userType == 'admin':
        appointments = appointments.order_by('date', 'startTime')

    else:
        appointments = appointments.filter(patient=user)
        appointments = appointments.annotate(
        is_upcoming=ExpressionWrapper(
            Q(date__gte=timezone.now().date()), 
            output_field=fields.BooleanField(),
        ),
    ).order_by('-is_upcoming', 'date', 'startTime')

 # excluding
    successful_payments = Payment.objects.filter(slot__in=appointments, is_successful=True)
    print(successful_payments)
    appointments = appointments.exclude(id__in=successful_payments.values('slot__id'))
    print(appointments)
   
    return render(
        request,
        'dashboard/appointment.html',
        {'appointments': appointments, }
    )

def historyAppointment(request):
    user = request.user

    if user.userprofile.userType == 'doctor':
        paidAppointments = Payment.objects.filter(
            slot__doctor=user.doctor,
            is_successful=True
        ).prefetch_related('slot__doctor__specialties')
        # print(paidAppointments)

    elif user.userprofile.userType == 'admin':
        paidAppointments = Payment.objects.filter(
            is_successful=True
        ).prefetch_related('slot__doctor__specialties')
        # print(paidAppointments)

    else:
        paidAppointments = Payment.objects.filter(
            slot__patient=user,
            is_successful=True
        )
        
    return render(request, 'dashboard/historyAppointment.html', {'paidAppointments': paidAppointments})



def cancelAppointment(request, appointmentId):
    appointment = get_object_or_404(Slot, pk=appointmentId)

    if (appointment.isBooked and
        (request.user.userprofile.userType == 'normal' and appointment.patient == request.user) or
        (request.user.userprofile.userType == 'doctor' and appointment.doctor.user == request.user) or
        (request.user.userprofile.userType == 'admin' )):
        
        appointment.patient = None
        appointment.isBooked = False
        appointment.save()
        messages.success(request, 'The appointment successfully cancel!')
    return redirect('userDoctorAppointment')



def createSlot(request):
    if request.user.userprofile.userType in ['doctor', 'admin']:
        if request.method == 'POST':
            form = SlotForm(request.POST)
            if form.is_valid():
                newSlot = form.save(commit=False)
                if request.user.userprofile.userType == 'doctor':
                    print('doctor')
                    newSlot.doctor = request.user
                elif request.user.userprofile.userType == 'admin':
                    selectedDoctor = form.cleaned_data.get('doctor')
                    print(selectedDoctor)
                    if selectedDoctor:
                        newSlot.doctor = selectedDoctor
                newSlot.save()
                messages.success(request, 'Slot created successfully.')
                return redirect('listUnbookedSlots')  
            else:
                print(form.errors)
        else:
            form = SlotForm()
        
        if request.user.userprofile.userType == 'admin':
            doctors = Doctor.objects.all()
            print(doctors,'admin')
        else:
            doctors = request.user
            print(doctors,'doctor')
        
        return render(request, 'dashboard/create-slot.html', {'form': form, 'doctors': doctors})
    return redirect('dashboard')



def addDoctorAddAdmin(request):
    if request.user.userprofile.userType == 'admin':
        users = User.objects.all()
    context = {'users': users}
    return render(request, 'dashboard/addDoctorAddAdmin.html', context)


def makeAdmin(request,userId):
    user=get_object_or_404(User,id=userId)
    # print(user)
    user.userprofile.userType = 'admin'
    user.userprofile.save()
    messages.success(request, f'{user.username} successfully become admin.')
    return redirect('addDoctorAddAdmin')

def addDoctor(request,userId):
    user =get_object_or_404(User,id=userId)
    print(user)
    if request.method == 'POST':
        form = AddDoctorForm(user,request.POST)
        if form.is_valid():
            user.userprofile.userType ='doctor'
            user.userprofile.save()
            doctor, created = Doctor.objects.get_or_create(user=user)
            specialties = form.cleaned_data['specialties']
            doctor.specialties.set(specialties)
            messages.success(request, f'Dr {user.username} successfully added.')
            return redirect('addDoctorAddAdmin')
    else:
        form = AddDoctorForm(user)
    context={'form':form,'user':user}
            
    return render(request,'dashboard/add-doctor.html',context)

def bookForConsultate(request):
    consultations = Consultation.objects.all()
    
    return render (request,'dashboard/bookForConsultate.html',{'consultations':consultations})

def makePayment(request, slotId):
    slot = get_object_or_404(Slot, id=slotId)
    
    try:
        payment = slot.payment
    except ObjectDoesNotExist:
        payment = None  

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.amount = form.cleaned_data['amount']
            payment.slot = slot  
            payment. is_successful=True
            payment.save()
            messages.success(request, 'Payment created successfully.')
            return redirect('historyAppointment')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'dashboard/payment.html', {'form': form, 'payment': payment, 'slot': slot})
    
def listUnbookedSlots(request):
    user = request.user

    if user.userprofile.userType == 'admin':
        unbookedSlots = Slot.objects.filter(isBooked=False).order_by('date', 'startTime')
    elif user.userprofile.userType == 'doctor':
        unbookedSlots = Slot.objects.filter(doctor=user.doctor, isBooked=False).order_by('date', 'startTime')
    # print(unbookedSlots)

    return render(request, 'dashboard/list-Unbooked-Slots.html', {'unbookedSlots': unbookedSlots})