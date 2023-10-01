from django.urls import path
from .views import dashboard,userDoctorAppointment,HistoryAppointment,cancelAppointment
urlpatterns = [
    
    path('dashboard/',dashboard,name='dashboard'),
    path('userDoctorAppointment/',userDoctorAppointment,name='userDoctorAppointment'),
    path('historyAppointment/',HistoryAppointment,name='HistoryAppointment'),
    path('cancelAppointment/<str:appointmentId>/',cancelAppointment,name='cancelAppointment')
    
]