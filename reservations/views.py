from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from movies.models import Session
from reservations.serializers import SeatSerializer, ReservationSerializer, TicketSerializer
from reservations.models import Seat, Reservation, Ticket


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
        if seat.status == 'reserved':
            reservation = Reservation.objects.filter(seat=seat, is_active=True).first()
            if reservation and reservation.reserved_until < timezone.now():
                seat.status = 'available'
                seat.save()
                reservation.is_active = False
                reservation.save()
        if seat.status != 'available':
            raise ValidationError('Seat is not available')
        reserved_until = timezone.now() + timedelta(minutes=10)
        seat.status = 'reserved'
        seat.save()
        serializer.save(user=self.request.user, reserved_until=reserved_until)


class CheckoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, reservation_id):
        reservation = get_object_or_404(Reservation, id=reservation_id)
        if reservation.is_active != True or reservation.reserved_until < timezone.now():
            raise ValidationError('Reservation is expired or inactive')
        seat = reservation.seat
        seat.status = 'purchased'
        seat.save()
        reservation.is_active = False
        reservation.save()
        ticket = Ticket.objects.create(user=request.user, reservation=reservation)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
