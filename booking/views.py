from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['status', 'table']
        input_formats = {
            'reservation_time': ['%H:%S']
        }

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
        # Retrieve reservation deails from the filled in form
        reservation_date = request.POST.get('reservation_date')
        reservation_time = request.POST.get('reservation_time')
        reservation_length = request.POST.get('reservation_length')
        number_of_guests = request.POST.get('number_of_guests')
        table_location = request.POST.get('table_location')

        # Convert reservation date and time  datetime
        from datetime import datetime, timedelta
        reservation_datetime = datetime.combine(datetime.strptime(reservation_date, '%Y-%m-%d').date(),
                                                datetime.strptime(reservation_time, '%H:%M').time())
        end_datetime = reservation_datetime + timedelta(hours=float(reservation_length))

        # Query reservations overlapping with the requested time slot
        overlapping_reservations = Reservation.objects.filter(
            reservation_date=reservation_date,
            reservation_time__lte=reservation_time,
            reservation_time__gt=end_datetime.time(),
            status='confirmed'
        ).select_related('table')

        # Get all tables available at the requested location
        available_tables = RestaurantTable.objects.filter(table_location=table_location)

        # Filter out tables that are already booked during the requested time slot
        for reservation in overlapping_reservations:
            available_tables = available_tables.exclude(id=reservation.table.id)

        return render(request, 'booking/available_tables.html', {'available_tables': available_tables})

    # If request method is not POST, render the reservation form
    return render(request, 'booking/booking_form.html')