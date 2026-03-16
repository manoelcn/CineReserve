import uuid
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

    def __str__(self):
        return f"{self.seat_number} - {self.session}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservations')
    reserved_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.seat.seat_number} - {self.user.username}"


class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='ticket')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)
