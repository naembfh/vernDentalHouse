from django.shortcuts import render, get_object_or_404
from .models import DentalService, Doctor, Slot
from django.http import JsonResponse
from django.urls import reverse
def slots(request, serviceId):
    dentalService = get_object_or_404(DentalService, id=serviceId)
    # print(dentalService)
    doctors = Doctor.objects.all()
    # print(doctors)
    slotsInfo = []
    for doctor in doctors:
        if dentalService in doctor.specialties.all():
            slots = Slot.objects.filter(doctor=doctor)
            # print(slots)
            for slot in slots:
                # print(slot.date)
                if slot.isBooked is False:
                     userProfile = doctor.user.userprofile
                    #  print(userProfile)
                     doctorPhoto = userProfile.userImage if userProfile else None
                     slotsInfo.append({
                    'id':slot.id,
                    'doctorName': doctor.user.username,
                    # 'doctorPhoto': doctor.user.userProfile.image,
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

            # Get the URL for the dashboard
            dashboard_url = reverse('dashboard')  # Replace 'dashboard' with the name of your dashboard URL pattern

            return JsonResponse({'success': True, 'message': 'Appointment booked successfully', 'dashboard_url': dashboard_url})

        return JsonResponse({'success': False, 'message': 'This slot is already booked'})

    return render(request, 'base/appointment.html')