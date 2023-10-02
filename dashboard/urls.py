from django.urls import path
from .views import dashboard,userDoctorAppointment,historyAppointment,cancelAppointment,createSlot,addDoctorAddAdmin,makeAdmin,addDoctor,bookForConsultate,makePayment
urlpatterns = [
    
    path('dashboard/',dashboard,name='dashboard'),
    path('userDoctorAppointment/',userDoctorAppointment,name='userDoctorAppointment'),
    path('historyAppointment/',historyAppointment,name='historyAppointment'),
    path('cancelAppointment/<str:appointmentId>/',cancelAppointment,name='cancelAppointment'),
    path('createSlot/',createSlot,name='createSlot'),
    path('addDoctorAddAdmin',addDoctorAddAdmin,name='addDoctorAddAdmin'),
    path('makeAdmin/<str:userId>/',makeAdmin,name='makeAdmin'),
    path('addDoctor/<str:userId>/',addDoctor,name='addDoctor'),
    path('bookForConsultate/',bookForConsultate,name='bookForConsultate'),
    path('makePayment/<str:slotId>/',makePayment,name='makePayment'),
    
]