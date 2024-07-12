from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from datetime import datetime, timedelta
from .models import Reservation, RestaurantTable, ExceptionalOpeningHours, NormalOpeningHours
from .forms import ReservationForm, CustomSignupForm, CustomUserChangeForm, ContactForm, EditReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import os
from datetime import datetime, time
from django.db.models import Max, Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import smtplib
from urllib.parse import urlencode
from django.utils import formats

class ReservationView(LoginRequiredMixin, FormView):
    template_name = 'booking/booking_form.html'
    form_class = ReservationForm
    success_url = '/thank_you/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Automatically set the user
        return super().form_valid(form)

def thank_you(request):
    return render(request, 'booking/thank_you.html')



def home(request):
    return render(request, 'booking/index.html')

def check_availability(request, reservation_id=None):
    # Initialize variables 
    available_tables = []
    alert_message = ""
    max_capacity = 0
    reservation = None

    # Determine if this is an edit operation
    is_edit = request.POST.get('is_edit') == 'true'

    if is_edit and reservation_id:
        try:
            reservation = Reservation.objects.get(reservation_id=reservation_id)
        except Reservation.DoesNotExist:
            return render(request, 'booking/booking_form.html', {
                'form': ReservationForm(),  # Provide a new form instance
                'available_tables': available_tables,
                'max_capacity': max_capacity,
                'alert_message': "Reservation does not exist.",
            })

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)

        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time_str = form.cleaned_data['reservation_time']
            reservation_time = datetime.strptime(reservation_time_str, "%H:%M").time()
            reservation_length = form.cleaned_data['reservation_length']
            table_location = form.cleaned_data['table_location']
            number_of_guests = form.cleaned_data['number_of_guests']
            message = form.cleaned_data.get('message', '')

            reservation_datetime = datetime.combine(reservation_date, reservation_time)
            end_datetime = reservation_datetime + timedelta(hours=reservation_length)

            available_tables = RestaurantTable.objects.filter(table_location=table_location, capacity__gte=number_of_guests)

            overlapping_bookings = Reservation.objects.filter(
                reservation_date=reservation_date,
                table__in=available_tables,
            ).filter(
                reservation_time__lt=end_datetime.time(),
                reservation_end_time__gt=reservation_time,
            )

            if is_edit and reservation:
                overlapping_bookings = overlapping_bookings.exclude(reservation_id=reservation.reservation_id)

            available_tables = available_tables.exclude(id__in=overlapping_bookings.values_list('table_id', flat=True))

            min_capacity = number_of_guests
            max_capacity = RestaurantTable.objects.aggregate(max_capacity=Max('capacity'))['max_capacity']

            found_tables = False

            if number_of_guests > max_capacity or not available_tables.exists():
                formatted_reservation_date = formats.date_format(reservation_date, "d F Y")
                if number_of_guests > max_capacity:
                    subject = f"Booking Enquiry: {number_of_guests} people - {formatted_reservation_date} - {reservation_time_str} - {reservation_length} hours - {table_location}"
                    subject_param = urlencode({'subject': subject})
                    alert_message = f"If you wish to book a table for {number_of_guests} people, please <a href='{reverse('contact')}?{subject_param}&message={message}'>contact us using the contact form</a>."
                else:
                    subject = f"Booking Enquiry: {number_of_guests} people - {formatted_reservation_date} - {reservation_time_str} - {reservation_length} hours - {table_location}"
                    subject_param = urlencode({'subject': subject})
                    alert_message = f"Unfortunately, we do not have a table available for your group of {number_of_guests} at the chosen time. Please <a href='{reverse('contact')}?{subject_param}&message={message}'>contact us using the contact form</a> for assistance, or try searching for another time or date."

            for capacity in range(min_capacity, max_capacity + 1):
                filtered_tables = available_tables.filter(capacity=capacity)
                if filtered_tables.exists():
                    available_tables = filtered_tables
                    found_tables = True
                    break

            template_name = 'booking/edit_reservation.html' if is_edit else 'booking/booking_form.html'
            return render(request, template_name, {
                'form': form,
                'available_tables': available_tables,
                'max_capacity': max_capacity,
                'alert_message': alert_message,
                'reservation': reservation,
            })

        else:
            print("Form is invalid")
            print(form.errors)

    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'booking/booking_form.html', {
        'form': form,
        'available_tables': available_tables,
        'max_capacity': max_capacity,
        'alert_message': alert_message,
        'reservation': reservation,
    })

# def check_availability(request, reservation_id=None):
#     # Initialise variables 
#     available_tables = []
#     alert_message = ""
#     max_capacity = 0
#     reservation_id = request.POST.get('reservation_id')
#     is_edit = request.POST.get('is_edit') == 'true'


#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation_date = form.cleaned_data['reservation_date']
#             reservation_time_str = form.cleaned_data['reservation_time']
#             print("reservation_time_str:", reservation_time_str)
#             print("reservation_time_str TYPE :", type(reservation_time_str))
#             reservation_time = datetime.strptime(reservation_time_str, "%H:%M").time()
#             print("reservation_time TYPE :", type(reservation_time))
#             reservation_length = form.cleaned_data['reservation_length']
#             print("reservation_length check: ", reservation_length)
#             table_location = form.cleaned_data['table_location']
#             print("table location: ", table_location)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             number_of_guests = form.cleaned_data['number_of_guests']
#             print("number of guests: ", number_of_guests)
#             message = form.cleaned_data.get('message', '')

#             # Convert reservation_time from string to time object
#             # reservation_time = datetime.strptime(reservation_time_str, '%H:%M').time()
#             reservation_datetime = datetime.combine(reservation_date, reservation_time)
#             end_datetime = reservation_datetime + timedelta(hours=reservation_length)

            
#             available_tables = RestaurantTable.objects.filter(table_location=table_location, capacity__gte=number_of_guests)
#             print("Available tables:", available_tables)

#             # available_tables = RestaurantTable.objects
#             # print("Available tables: ", available_tables)

#             # # Find all tables in the specified location
#             # available_tables = available_tables.filter(table_location=table_location)
#             # print("Available tables: ", available_tables)

#             # # Filter out tables wiht capacity is less than the number of guests
#             # available_tables = available_tables.filter(capacity__gte=number_of_guests)

#             # print("Available tables: ", available_tables)

#             # Check for overlapping bookings and exclude tables with such bookings
#             overlapping_bookings = Reservation.objects.filter(
#                 reservation_date=reservation_date,
#                 table__in=available_tables,
#             ).filter(
#                 reservation_time__lt=end_datetime.time(),
#                 reservation_end_time__gt=reservation_time,
#             )

#             if reservation_id:
#                 print("ID IS BEING RECEIVED")
#                 overlapping_bookings = overlapping_bookings.exclude(reservation_id=reservation_id)

#             available_tables = available_tables.exclude(id__in=overlapping_bookings.values_list('table_id', flat=True))
            
#             # Initialize variables for finding the smallest available table that fits the group size
#             min_capacity = number_of_guests
#             print("MIN_CAPACITY: ", min_capacity)
#             max_capacity = RestaurantTable.objects.aggregate(max_capacity=Max('capacity'))['max_capacity']
#             print("MAX_CAPACITY: ", max_capacity)

#             found_tables = False

#             # Check if number of guests exceeds the largest table capacity or no tables are available
#             # Determine availability message
#             if number_of_guests > max_capacity or not available_tables.exists():
#                 formatted_reservation_date = formats.date_format(reservation_date, "d F Y")
#                 if number_of_guests > max_capacity:
#                     subject = f"Booking Enquiry: {number_of_guests} people - {formatted_reservation_date} - {reservation_time_str} - {reservation_length} hours - {table_location}"
#                     subject_param = urlencode({'subject': subject})
#                     alert_message = f"If you wish to book a table for {number_of_guests} people, please <a href='{reverse('contact')}?{subject_param}&message={message}'>contact us using the contact form</a>."
#                 else:
#                     subject = f"Booking Enquiry: {number_of_guests} people - {formatted_reservation_date} - {reservation_time_str} - {reservation_length} hours - {table_location}"
#                     subject_param = urlencode({'subject': subject})
#                     alert_message = f"Unfortunately, we do not have a table available for your group of {number_of_guests} at the chosen time. Please <a href='{reverse('contact')}?{subject_param}&message={message}'>contact us using the contact form</a> for assistance, or try searching for another time or date."
#                     # available_tables = []



#             # Iterate from group size up to max_capacity to find the smallest available table
#             for capacity in range(min_capacity, max_capacity + 1):
#                 filtered_tables = available_tables.filter(capacity=capacity)
#                 if filtered_tables.exists():
#                     available_tables = filtered_tables
#                     found_tables = True
#                     break

#             template_name = 'booking/edit_reservation.html' if is_edit else 'booking/booking_form.html'

#             return render(request, template_name, {
#                 'form': form,
#                 'available_tables': available_tables,
#                 'max_capacity': max_capacity,
#                 'alert_message': alert_message,
#                 'reservation': Reservation.objects.get(reservation_id=reservation_id) if is_edit else None
#             })

#         else:
#             print("Form is invalid")
#             print(form.errors)

#         # return render(request, 'booking/booking_form.html', {
#         #     'form': form,
#         #     'available_tables': available_tables,
#         #     'max_capacity': max_capacity  # Pass max_capacity to the template
#         # })

#     else:
#         form = ReservationForm()

#     template_name = 'booking/edit_reservation.html' if is_edit else 'booking/booking_form.html'

#     return render(request, template_name, {
#         'form': form,
#         'available_tables': available_tables,
#         'max_capacity': max_capacity,
#         'alert_message': alert_message,
#         'reservation': Reservation.objects.get(reservation_id=reservation_id) if is_edit else None
#     })

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
                user=request.user,
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
            )
            new_booking.save()

            send_reservation_email(new_booking)

            return redirect('thank_you')
    else:
        form = ReservationForm(user=request.user)

    form = ReservationForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def get_opening_hours(request):
    date_str = request.GET.get('date')
    print("date_str: ", date_str)
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
        
        try:
            opening_hours = ExceptionalOpeningHours.objects.get(date=date)
            opening_time = opening_hours.opening_time.strftime('%H:%M') if opening_hours.opening_time else '00:00'
            closing_time = opening_hours.closing_time.strftime('%H:%M') if opening_hours.closing_time else '00:00'
            data = {
                'opening_time': opening_time,
                'closing_time': closing_time
            }
            print("Opening data retrieved from ExceptionalOpeningHours")
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
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/current_reservations.html', {'reservations': reservations})

def cancellation_confirmed(request):
    return render(request, 'booking/cancellation_confirmed.html')

@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(reservation_id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        send_reservation_email(reservation, is_creation=False)
        return redirect('cancellation_confirmed')
    
    return render(request, 'booking/cancel_reservation.html', {'reservation': reservation})

def send_reservation_email(reservation, is_creation=True):

    print("is_creation: ", is_creation)

    subject_guest = 'BigByte - Reservation Confirmation' if is_creation else 'BigByte - Reservation Cancellation'
    subject_restaurant = 'New Reservation' if is_creation else 'Reservation Cancelled'
    template_guest = 'booking/reservation_confirmation_guest.html' if is_creation else 'booking/reservation_cancellation_guest.html'
    template_restaurant = 'booking/reservation_confirmation_restaurant.html' if is_creation else 'booking/reservation_cancellation_restaurant.html'

    # Format reservation length as "__ hours"
    reservation_length_str = f"{reservation.reservation_length} hours"

    # Format reservation time and end time as HH:MM
    reservation_time_str = reservation.reservation_time.strftime('%H:%M')
    reservation_end_time_str = reservation.reservation_end_time.strftime('%H:%M')

    # Context for guest and restaurant email
    context_email = {
        'guest_first_name': reservation.first_name,
        'guest_last_name': reservation.last_name,
        'reservation_date': reservation.reservation_date,
        'reservation_time': reservation_time_str,
        'reservation_end_time': reservation_end_time_str,
        'reservation_length': reservation_length_str,
        'message': reservation.message,
        'reservation': reservation
    }

    print("Context Email:", context_email)

    html_message_guest = render_to_string(template_guest, context_email)
    html_message_restaurant = render_to_string(template_restaurant, context_email)
    
    plain_message_guest = strip_tags(html_message_guest)
    plain_message_restaurant = strip_tags(html_message_restaurant)
    
    from_email = settings.DEFAULT_FROM_EMAIL
    to_guest = reservation.email
    to_restaurant = settings.RESTAURANT_EMAIL

    # Send email to the user
    send_mail(subject_guest, plain_message_guest, from_email, [to_guest], html_message=html_message_guest)

    # Send email to the restaurant
    send_mail(subject_restaurant, plain_message_restaurant, from_email, [to_restaurant], html_message=html_message_restaurant)








    # # Format reservation length as "__ hours"
    # reservation.reservation_length = f"{reservation.reservation_length} hours"

    # # Format reservation time and end time as HH:MM
    # reservation.reservation_time = reservation.reservation_time.strftime('%H:%M')
    # reservation.reservation_end_time = reservation.reservation_end_time.strftime('%H:%M')

    # subject_guest = 'BigByte - Reservation Confirmation'
    # subject_restaurant = 'New Reservation'
    # html_message_guest = render_to_string('booking/reservation_confirmation_guest.html', {'guest_first_name': reservation.first_name, 'guest_last_name': reservation.last_name, 'reservation': reservation})
    # html_message_restaurant = render_to_string('booking/reservation_confirmation_restaurant.html', {'guest_first_name': reservation.first_name, 'guest_last_name': reservation.last_name, 'reservation': reservation})
    # plain_message_guest = strip_tags(html_message_guest)
    # plain_message_restaurant = strip_tags(html_message_restaurant)
    # from_email = 'pp4restaurant@gmail.com'
    # to = reservation.email
    
    # plain_message_guest = strip_tags(html_message_guest)
    # plain_message_restaurant = strip_tags(html_message_restaurant)

#     # Send email to the user
#     send_mail(subject_guest, plain_message_guest, from_email, [to], html_message=html_message_guest)

#     # Send email to the restaurant
#     send_mail(subject_restaurant, plain_message_restaurant, from_email, [settings.EMAIL_HOST_USER], html_message=html_message_restaurant)

# def reservation_completed(request):
#     # Handle reservation logic
#     reservation = create_reservation(request) 

#     # Send confirmation email
#     send_reservation_email(reservation)

#     return render(request, 'thank_you.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            context_email = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'subject': subject,
                'message': message,
            }

            email_content = render_to_string('booking/contact_restaurant.html', context_email)

            plain_email_content = strip_tags(email_content)
    
            from_email = settings.DEFAULT_FROM_EMAIL
            to_restaurant = settings.RESTAURANT_EMAIL

            # Send email to the restaurant
            send_mail(subject, plain_email_content, from_email, [to_restaurant], html_message=email_content)

            return redirect('contact_success')

    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'subject': request.GET.get('subject', ''),
                'message': request.GET.get('message', ''),
            }
        
        form = ContactForm(initial=initial_data)
    return render(request, 'booking/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'booking/contact_success.html')

def update_confirmed(request):
    return render(request, 'booking/update_confirmed.html')

def edit_reservation(request, reservation_id):
    # Retrieve the reservation object based on the reservation_id
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    
    if request.method == 'POST':
        form = EditReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save()
            return redirect(request, 'booking/update_confirmed')
    else:
        # If the request method is GET, initialize the form with the existing reservation data
        form = EditReservationForm(instance=reservation)

    # Render the edit_reservation.html template with the form and reservation context
    return render(request, 'booking/edit_reservation.html', {'form': form, 'reservation': reservation})

def update_reservation(request, table_id):
    reservation_id = request.POST.get('reservation_id')
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)

    if request.method == 'POST':
        form = EditReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('update_confirmed')  # Redirect to update_confirmed view

    # Handle cases where the form is not valid or it's a GET request
    return redirect('edit_reservation', reservation_id=reservation_id)