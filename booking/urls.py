from django.urls import path
from .views import ReservationView, check_availability, home, thank_you

urlpatterns = [
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('check_availability/', check_availability, name='check_availability'),
    path('thank_you/', thank_you, name='thank_you'),
]