from rest_framework import serializers
from reservations.models import Seat, Reservation


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
