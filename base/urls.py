from django.urls import path
from .views import home
urlpatterns = [
    path('',home,name='home'),
    # path('dashboard/',dashboard,name='dashboard'),
    # path('userDoctorAppointment/',userDoctorAppointment,name='userDoctorAppointment')
    
]
