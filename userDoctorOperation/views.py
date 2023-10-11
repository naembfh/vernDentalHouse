from django.shortcuts import render, get_object_or_404
from .models import DentalService, Doctor, Slot
from django.http import JsonResponse
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib import messages

def slots(request, serviceId):
    dentalService = get_object_or_404(DentalService, id=serviceId)
    doctors = Doctor.objects.all()
    slotsInfo = []
    
    currentDatetime = timezone.now()  # Get the current date and time in the correct time zone
    
    for doctor in doctors:
        if dentalService in doctor.specialties.all():
            slots = Slot.objects.filter(doctor=doctor).order_by('date', 'startTime')
            for slot in slots:
                if not slot.isBooked:
                    # Ensure both the slot's datetime and current datetime are in the same time zone
                    slotDatetime = timezone.make_aware(datetime.combine(slot.date, slot.startTime), timezone=timezone.get_current_timezone())
                    
                    # Compare the slot's datetime with the current datetime
                    if slotDatetime >= currentDatetime:
                        userProfile = doctor.user.userprofile
                        doctorPhoto = userProfile.userImage if userProfile else None
                        
                        slotsInfo.append({
                            'id': slot.id,
                            'doctorName': doctor.user.username,
                            'doctorPhoto': doctorPhoto,
                            'slotDate': slot.date,
                            'slotStartTime': slot.startTime,
                            'slotEndTime': slot.endTime,
                        })

    context = {
        'dentalService': dentalService,
        'slotsInfo': slotsInfo,
    }

    return render(request, 'userDoctorOperation/slots.html', context)

def bookAppointment(request):
    if request.method == 'POST':
        slot_id = request.POST.get('slotId')
        slot = get_object_or_404(Slot, id=slot_id)

        if not slot.isBooked:
            slot.isBooked = True
            slot.patient = request.user
            slot.save()

            messages.success(request, 'Appointment created successfully.')
            dashboard_url = reverse('userDoctorAppointment')  

            return JsonResponse({'success': True, 'message': 'Appointment booked successfully', 'dashboard_url': dashboard_url})

        return JsonResponse({'success': False, 'message': 'This slot is already booked'})

    return render(request, 'base/appointment.html')