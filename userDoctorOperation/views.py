from django.shortcuts import render, get_object_or_404
from .models import DentalService, Doctor, Slot
from django.http import JsonResponse
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
                     slotsInfo.append({
                    'id':slot.id,
                    'doctorName': doctor.user.username,
                    'doctorPhoto': doctor.user.image,
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
    # print('here')
    if request.method == 'POST':
        # print('inside')
       
        slotId= request.POST.get('slotId')
        # print(slotId)
        slot = get_object_or_404(Slot, id=slotId)
        # print(slot)

        if not slot.isBooked:
            slot.isBooked = True
            slot.patient = request.user 
            slot.save()

            return JsonResponse({'message': 'Appointment booked successfully'})

        return JsonResponse({'message': 'This slot is already booked'})

    return render(request, 'base/appointment.html')