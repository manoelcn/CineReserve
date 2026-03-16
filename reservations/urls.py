from django.urls import path
from reservations.views import SeatListView, ReservationCreateView

urlpatterns = [
    path('sessions/<int:session_id>/seats/', SeatListView.as_view(), name='seat-list'),
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
]