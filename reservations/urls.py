from django.urls import path
from reservations.views import SeatListView, ReservationCreateView, CheckoutView, TicketListView

urlpatterns = [
    path('sessions/<int:session_id>/seats/', SeatListView.as_view(), name='seat-list'),
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:reservation_id>/checkout/', CheckoutView.as_view(), name='checkout'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
]