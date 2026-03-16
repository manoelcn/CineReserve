from rest_framework import serializers
from reservations.models import Seat, Reservation, Ticket


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
        extra_kwargs = {
            'reserved_until': {'read_only': True},
            'user': {'read_only': True},
        }


class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = ('id', 'code', 'created_at', 'user',)
        read_only_fields = ('id', 'code', 'created_at', 'user',)
