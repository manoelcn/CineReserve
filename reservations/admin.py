from django.contrib import admin
from reservations.models import Seat, Reservation, Ticket


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'seat_number', 'status')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'seat', 'reserved_until', 'is_active')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'user', 'code', 'created_at')
