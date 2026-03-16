from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from movies.models import Session
from reservations.serializers import SeatSerializer, ReservationSerializer
from reservations.models import Seat, Reservation


class SeatListView(ListAPIView):
    serializer_class = SeatSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        session_id = self.kwargs.get('session_id')
        session = get_object_or_404(Session, id=session_id)
        seats = Seat.objects.filter(session=session)
        return seats


class ReservationCreateView(CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        seat = serializer.validated_data.get('seat')
        if seat.status != 'available':
            raise ValidationError
        reserved_until = timezone.now() + timedelta(minutes=10)
        seat.status = 'reserved'
        seat.save()
        serializer.save(user=self.request.user, reserved_until=reserved_until)
