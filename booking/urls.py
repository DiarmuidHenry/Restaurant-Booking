from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
]