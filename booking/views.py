from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from .models import Reservation, RestaurantTable, ExceptionalOpeningHours, NormalOpeningHours
from .forms import ReservationForm, CustomSignupForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime
from datetime import datetime, time
from django.db.models import Max

class ReservationView(LoginRequiredMixin, FormView):
    template_name = 'booking/booking_form.html'
    form_class = ReservationForm
    success_url = '/thank_you/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        print("Form is valid")
        form.save()
        return super().form_valid(form)

def thank_you(request):
    return render(request, 'booking/thank_you.html')

def home(request):
    return render(request, 'booking/index.html')

def check_availability(request):
    available_tables = []
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time_str = form.cleaned_data['reservation_time']
            print("reservation_time_str:", reservation_time_str)
            print("reservation_time_str TYPE :", type(reservation_time_str))
            reservation_time = datetime.strptime(reservation_time_str, "%H:%M").time()
            print("reservation_time TYPE :", type(reservation_time))
            reservation_length = form.cleaned_data['reservation_length']
            print("reservation_length check: ", reservation_length)
            table_location = form.cleaned_data['table_location']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            number_of_guests = form.cleaned_data['number_of_guests']
            message = form.cleaned_data.get('message', '')

            # Convert reservation_time from string to time object
            # reservation_time = datetime.strptime(reservation_time_str, '%H:%M').time()
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

            # Initialize variables for finding the smallest available table that fits the group size
            min_capacity = number_of_guests
            max_capacity = available_tables.aggregate(max_capacity=Max('capacity'))['max_capacity']

            found_tables = False

            # Iterate from group size up to max_capacity to find the smallest available table
            for capacity in range(min_capacity, max_capacity + 1):
                filtered_tables = available_tables.filter(capacity=capacity)
                if filtered_tables.exists():
                    available_tables = filtered_tables
                    found_tables = True
                    break

            # If no exact match was found, look for larger tables step by step
            # if not found_tables:
            #     for capacity in range(min_capacity + 1, max_capacity + 1):
            #         filtered_tables = available_tables.filter(capacity=capacity)
            #         if filtered_tables.exists():
            #             available_tables = filtered_tables
            #             break


            # for booking in overlapping_bookings:
            #     available_tables = available_tables.exclude(id=booking.table.id)

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
            table_location = form.cleaned_data['table_location']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            number_of_guests = form.cleaned_data['number_of_guests']
            message = form.cleaned_data.get('message', '')

            reservation_time = datetime.strptime(reservation_time_str, "%H:%M").time()
            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            reservation_end_datetime = reservation_datetime + timedelta(hours=(reservation_length-1), minutes=59)
            reservation_end_time = reservation_end_datetime.time()

            table = RestaurantTable.objects.get(id=table_id)
            new_booking = Reservation.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                table=table,
                table_location=table_location,
                reservation_date=reservation_date,
                reservation_time=reservation_time,
                reservation_length=reservation_length,
                reservation_end_time=reservation_end_time,
                number_of_guests=number_of_guests,
                message=message,
                status='confirmed' 
            )
            new_booking.save()

            return redirect('thank_you')
    else:
        form = ReservationForm(user=request.user)

    form = ReservationForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def get_opening_hours(request):
    date_str = request.GET.get('date')
    
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
        
        try:
            opening_hours = ExceptionalOpeningHours.objects.get(date=date)
            data = {
                'opening_time': opening_hours.opening_time.strftime('%H:%M'),
                'closing_time': opening_hours.closing_time.strftime('%H:%M')
            }
            print("Opening data retreived from ExceptionalOpeningHours")
        except ExceptionalOpeningHours.DoesNotExist:
            try:
                opening_hours = NormalOpeningHours.objects.get(day=date.strftime('%A').lower())
                data = {
                    'opening_time': opening_hours.opening_time.strftime('%H:%M'),
                    'closing_time': opening_hours.closing_time.strftime('%H:%M')
                }
                print("Opening data retreived from NormalOpeningHours")
            except NormalOpeningHours.DoesNotExist:
                data = {'error': 'No opening hours found for this date'}
    else:
        data = {'error': 'No date provided'}
    
    return JsonResponse(data)
    
@login_required
def current_reservations(request):
    reservations = Reservation.objects.filter(email=request.user.email)
    return render(request, 'booking/current_reservations.html', {'reservations': reservations})

@login_required
def edit_reservation(request, reservation_id):
    reservation = Reservation.objects.get(reservation_id=reservation_id, email=request.user.email)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('current_reservations')
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'booking/edit_reservation.html', {'form': form, 'reservation': reservation})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(reservation_id=reservation_id, email=request.user.email)
    if request.method == 'POST':
        reservation.delete()
        return redirect('current_reservations')
    
    return render(request, 'booking/cancel_reservation.html', {'reservation': reservation})