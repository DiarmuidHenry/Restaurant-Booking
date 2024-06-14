from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Reservation, RestaurantTable
from .forms import ReservationForm

class ReservationView(FormView):
    template_name = 'booking/booking_form.html'
    form_class = ReservationForm
    success_url = '/thank_you/'

    def form_valid(self, form):
        print("Form is valid")
        form.save()
        return super().form_valid(form)

def thank_you(request):
    return render(request, 'booking/thank_you.html')

def home(request):
    return render(request, 'booking/home.html')

def check_availability(request):
    available_tables = []
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time_str = form.cleaned_data['reservation_time']
            reservation_length = form.cleaned_data['reservation_length']
            table_location = form.cleaned_data['table_location']
            number_of_guests = form.cleaned_data['number_of_guests']

            # Convert reservation_time from string to time object
            reservation_time = datetime.strptime(reservation_time_str, '%H:%M').time()
            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            end_datetime = reservation_datetime + timedelta(hours=reservation_length)

            # Find all tables in the specified location
            available_tables = RestaurantTable.objects.filter(table_location=table_location)

            # Check for overlapping bookings and exclude tables with such bookings
            overlapping_bookings = Reservation.objects.filter(
                reservation_date=reservation_date,
                table__in=available_tables
            ).filter(
                reservation_time__lt=end_datetime.time(),
                reservation_end_time__gt=reservation_time
            )

            # Filter out tables wiht capacity is less than the number of guests
            available_tables = available_tables.filter(capacity__gte=number_of_guests)

            for booking in overlapping_bookings:
                available_tables = available_tables.exclude(id=booking.table.id)

        else:
            print("Form is invalid")
            print(form.errors)

        return render(request, 'booking/booking_form.html', {
            'form': form,
            'available_tables': available_tables
        })

    else:
        form = ReservationForm()

    return render(request, 'booking/booking_form.html', {
        'form': form,
        'available_tables': available_tables
    })

def make_reservation(request, table_id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time_str = form.cleaned_data['reservation_time']
            reservation_length = form.cleaned_data['reservation_length']
            customer_name = form.cleaned_data['customer_name']
            number_of_guests = form.cleaned_data['number_of_guests']

            reservation_time = datetime.strptime(reservation_time_str, "%H:%M").time()
            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            end_datetime = reservation_datetime + timedelta(hours=reservation_length)

            table = RestaurantTable.objects.get(id=table_id)
            new_booking = Reservation.objects.create(
                customer_name=customer_name,
                table=table,
                reservation_date=reservation_date,
                reservation_time=reservation_time,
                reservation_length=reservation_length,
                number_of_guests=number_of_guests,
                status='confirmed'  # assuming 'confirmed' is the correct status
            )
            new_booking.save()

            return redirect('thank_you')

    form = ReservationForm()
    return render(request, 'booking/booking_form.html', {'form': form})