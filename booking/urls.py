from django.urls import path
from . import views
from .views import ReservationView

urlpatterns = [
    path('', views.home, name='home'), 
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('thank_you/', views.thank_you, name='thank_you'),
]