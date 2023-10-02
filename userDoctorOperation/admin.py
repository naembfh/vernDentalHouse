from django.contrib import admin
from .models import Doctor,Slot,Payment
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Slot)
admin.site.register(Payment)

