from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Reservation, RestaurantTable, TableBooking
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
    if request.method == 'POST':
        # Retrieve reservation details from filled-in form
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            reservation_length = form.cleaned_data['reservation_length']
            table_location = form.cleaned_data['table_location']

            # Convert reservation_time_str to a datetime.time object
            reservation_time = datetime.strptime(reservation_time, "%H:%M").time()
            
            # Calculate reservation end time
            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            end_datetime = reservation_datetime + timedelta(hours=reservation_length)

            # Check if any bookings overlap with requested time slot
            overlapping_bookings = TableBooking.objects.filter(
                reservation_date=reservation_date,
                reservation_time__lt=end_datetime.time()
            ).exclude(
                reservation_time__gte=end_datetime.time()
            )

            # Get all tables available in requested location
            available_tables = RestaurantTable.objects.filter(table_location=table_location)

            # Filter out tables that are already booked during requested time 
            for booking in overlapping_bookings:
                available_tables = available_tables.exclude(id=booking.table.id)

            return render(request, 'booking/available_tables.html', {'available_tables': available_tables})

    # If request method is not POST or form is invalid, just render reservation form
    form = ReservationForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def make_reservation(request, table_id):
    if request.method == 'POST':
        # Retrieve reservation details from form
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            reservation_length = form.cleaned_data['reservation_length']

            # Convert reservation_time_str to a datetime.time object
            reservation_time = datetime.strptime(reservation_time, "%H:%M").time()
            
            # Calculate reservation end time
            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            end_datetime = reservation_datetime + timedelta(hours=reservation_length)
            
            # Create new booking for the selected table
            table = RestaurantTable.objects.get(id=table_id)
            booking = TableBooking.objects.create(
                table=table,
                reservation_date=reservation_date,
                reservation_time=reservation_time,
                duration=reservation_length
            )
            booking.save()

            # Redirect to thank_you page
            return redirect('thank_you')

    # If request method is not POST or form is invalid, just render reservation form again
    form = ReservationForm()
    return render(request, 'booking/booking_form.html', {'form': form})