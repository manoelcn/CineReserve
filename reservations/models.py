from django.db import models
from authentication.models import User
from movies.models import Session

STATUS_CHOICES = [
    ('available', 'Available'),
    ('reserved', 'Reserved'),
    ('purchased', 'Purchased'),
]

class Seat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservations')
    reserved_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
