from django.urls import path
from .views import ReservationView, check_availability, home, thank_you, make_reservation, get_opening_hours, current_reservations, cancel_reservation, cancellation_confirmed, contact, contact_success, edit_reservation, update_confirmed

urlpatterns = [
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('check_availability/', check_availability, name='check_availability'),
    path('check_availability/<int:reservation_id>/', check_availability, name='check_availability_edit'),
    path('thank_you/', thank_you, name='thank_you'),
    path('cancellation_confirmed', cancellation_confirmed, name='cancellation_confirmed'),
    path('make_reservation/<int:table_id>/', make_reservation, name='make_reservation'),
    path('reservation/get_opening_hours/', get_opening_hours, name='get_opening_hours'),
    path('cancel_reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    # path('profile/', profile_view, name='profile'),
    path('current_reservations/', current_reservations, name='current_reservations'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('reservation/<int:reservation_id>/edit/', edit_reservation, name='edit_reservation'),
    path('reservation/<int:reservation_id>/<int:table_id>/', edit_reservation, name='edit_reservation'),
    path('update_confirmed/', update_confirmed, name='update_confirmed')
]

