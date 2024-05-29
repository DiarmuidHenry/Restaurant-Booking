from django.urls import path
from . import views
from .views import ReservationView, check_availability

urlpatterns = [
    path('', views.home, name='home'), 
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('check_availability/', check_availability, name='check_availability'),
    path('thank_you/', views.thank_you, name='thank_you'),
]