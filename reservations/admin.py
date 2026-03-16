from django.contrib import admin
from reservations.models import Seat, Reservation


admin.site.register(Seat)
admin.site.register(Reservation)
