from django.shortcuts import render
from userDoctorOperation.models import Slot
# Create your views here.
def dashboard(request):
    return render(request,'dashboard/dashboard.html')
# user action

def userDoctorAppointment(request):
    page = 'userDoctorAppointment'
    user = request.user

    if user.userprofile.userType == 'doctor':
        # Fetch doctor's current appointments
        appointments = Slot.objects.filter(doctor=user.doctor, isBooked=True)
        print(appointments)
    else:
        # Fetch normal user's current appointments
        appointments = Slot.objects.filter(patient=user, isBooked=True)

    return render(
        request,
        'dashboard/appointment.html',
        {'appointments': appointments, 'page': userDoctorAppointment}
    )

def HistoryAppointment(request):
    return render(request,'dashboard/historyAppointment.html')

from django.shortcuts import get_object_or_404, redirect

def cancelAppointment(request, appointmentId):
    appointment = get_object_or_404(Slot, pk=appointmentId)

    # Check if the user is authorized to cancel the appointment
    if (appointment.isBooked and
        (request.user.userprofile.userType == 'normal' and appointment.patient == request.user) or
        (request.user.userprofile.userType == 'doctor' and appointment.doctor.user == request.user)):
        # Set patient to null and isBooked to False
        appointment.patient = None
        appointment.isBooked = False
        appointment.save()

    # Redirect to the appointment list view or a confirmation page
    return redirect('userDoctorAppointment')
