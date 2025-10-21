from django.contrib import admin
from .models import Court, TimeSlot, Reservation, Teamers

# Register your models here.
admin.site.register(Court)
admin.site.register(TimeSlot)
admin.site.register(Reservation)
admin.site.register(Teamers)
