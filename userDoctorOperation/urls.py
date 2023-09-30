from django.urls import path
from .views import slots,bookAppointment
urlpatterns = [
    path('slots/<str:serviceId>/', slots, name='slots'),
    path('bookAppointment/',bookAppointment,name='bookAppointment'),
]
