from django.urls import path
from .views import ReservationView, check_availability, home, thank_you, make_reservation, get_opening_hours

urlpatterns = [
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('check_availability/', check_availability, name='check_availability'),
    path('thank_you/', thank_you, name='thank_you'),
    path('make_reservation/<int:table_id>/', make_reservation, name='make_reservation'),
    path('reservation/get_opening_hours/', get_opening_hours, name='get_opening_hours'),  # Ensure this line

]