from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse
from datetime import datetime, timedelta
from .models import (
    Reservation,
    RestaurantTable,
    ExceptionalOpeningHours,
    NormalOpeningHours)
from .forms import (
    ReservationForm,
    CustomSignupForm,
    CustomUserChangeForm,
    ContactForm,
    EditReservationForm)
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
    # Initialise variables
    available_tables = []
    alert_message = ""
    max_capacity = 0
    reservation = None

    # Determine if this is an edit operation
    is_edit = request.POST.get('is_edit') == 'true'

    # Fetch reservation info, if in edit resrvation
    if is_edit and reservation_id:
        try:
            reservation = (
                Reservation.objects.get(reservation_id=reservation_id))
        except Reservation.DoesNotExist:
            return render(request, 'booking/booking_form.html', {
                'form': ReservationForm(),  # Provide a new form instance
                'available_tables': available_tables,
                'max_capacity': max_capacity,
                'alert_message': "Reservation does not exist.",
            })

    # Get info from form
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)

        if form.is_valid():
            number_of_guests = form.cleaned_data['number_of_guests']
            if not 1 <= number_of_guests <= 50:
                form.add_error(
                    'number_of_guests',
                    'Number of guests must be between 1 and 50.')
                return render(request, 'booking/booking_form.html', {
                    'form': form,
                    'available_tables': available_tables,
                    'max_capacity': max_capacity,
                    'alert_message': alert_message,
                    'reservation': reservation,
                })
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time_str = form.cleaned_data['reservation_time']
            reservation_time = (
                datetime.strptime(reservation_time_str, "%H:%M").time())
            reservation_length = form.cleaned_data['reservation_length']
            table_location = form.cleaned_data['table_location']
            number_of_guests = form.cleaned_data['number_of_guests']
            message = form.cleaned_data.get('message', '')

            reservation_datetime = (
                datetime.combine(reservation_date, reservation_time))
            end_datetime = (
                reservation_datetime + timedelta(hours=reservation_length))

            # Filter/check all tables for a suitable match
            available_tables = (
                RestaurantTable.objects.filter(
                    table_location=table_location,
                    capacity__gte=number_of_guests))

            overlapping_bookings = Reservation.objects.filter(
                reservation_date=reservation_date,
                table__in=available_tables,
            ).filter(
                reservation_time__lt=end_datetime.time(),
                reservation_end_time__gt=reservation_time,
            )

            # If editing reservation, exclude this from search
            if is_edit and reservation:
                overlapping_bookings = (
                    overlapping_bookings.exclude(
                        reservation_id=reservation.reservation_id))

            available_tables = (
                available_tables.exclude(
                    id__in=overlapping_bookings.values_list(
                        'table_id', flat=True)))

            # Find smallest matching table
            min_capacity = number_of_guests
            max_capacity = (
                RestaurantTable.objects.aggregate(
                    max_capacity=Max('capacity'))['max_capacity'])

            found_tables = False

            if number_of_guests > max_capacity or not (
                    available_tables.exists()):
                formatted_reservation_date = (
                    formats.date_format(reservation_date, "d F Y"))
                subject = (
                        f"Booking Enquiry: {number_of_guests} people "
                        f"- {formatted_reservation_date} - "
                        f"{reservation_time_str} "
                        f"- {reservation_length} hours - {table_location}")
                subject_param = urlencode({'subject': subject})
                if number_of_guests > max_capacity:
                    alert_message = f"""
                    If you wish to book a table for
                     {number_of_guests} people, please
                     <a href='{reverse('contact')}?{(
                     subject_param)}&message={message}'>contact us
                     using the contact form</a>.
                    """
                else:
                    alert_message = f"""
                    Unfortunately, we do not have a table
                     available for your group of {number_of_guests} at the
                     chosen time. Please <a href='{reverse('contact')}?
                    {subject_param}&message={message}'>contact us using the
                     contact form</a> for assistance, or try searching
                     for another time or date.
                    """

            for capacity in range(min_capacity, max_capacity + 1):
                filtered_tables = available_tables.filter(capacity=capacity)
                if filtered_tables.exists():
                    available_tables = filtered_tables
                    found_tables = True
                    break

            template_name = (
                'booking/edit_reservation.html' if is_edit else (
                    'booking/booking_form.html'))
            return render(request, template_name, {
                'form': form,
                'available_tables': available_tables,
                'max_capacity': max_capacity,
                'alert_message': alert_message,
                'reservation': reservation,
            })

    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'booking/booking_form.html', {
        'form': form,
        'available_tables': available_tables,
        'max_capacity': max_capacity,
        'alert_message': alert_message,
        'reservation': reservation,
    })


def get_opening_hours(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse(
                {'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        try:
            opening_hours = ExceptionalOpeningHours.objects.get(date=date)
            opening_time = (
                opening_hours.opening_time.strftime('%H:%M') if (
                    opening_hours.opening_time) else '00:00')
            closing_time = (
                opening_hours.closing_time.strftime('%H:%M') if (
                    opening_hours.closing_time) else '00:00')
            data = {
                'opening_time': opening_time,
                'closing_time': closing_time
            }
        except ExceptionalOpeningHours.DoesNotExist:
            try:
                opening_hours = (
                    NormalOpeningHours.objects.get(
                        day=date.strftime('%A').lower()))
                data = {
                    'opening_time': (
                        opening_hours.opening_time.strftime('%H:%M')),
                    'closing_time': (
                        opening_hours.closing_time.strftime('%H:%M'))
                }
            except NormalOpeningHours.DoesNotExist:
                data = {'error': 'No opening hours found for this date'}
    else:
        data = {'error': 'No date provided'}

    return JsonResponse(data)


@login_required
def current_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(
        request,
        'booking/current_reservations.html',
        {'reservations': reservations})


def cancellation_confirmed(request):
    return render(
        request,
        'booking/cancellation_confirmed.html')


@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(
        reservation_id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        send_reservation_email(reservation, 'cancel')
        return redirect('cancellation_confirmed')

    return render(
        request,
        'booking/cancel_reservation.html',
        {'reservation': reservation})


# Controls all confirmation emails
def send_reservation_email(
        reservation,
        action='create',
        previous_reservation=None):

    # Initialise variables for reservation info
    reservation_date = ''
    reservation_time_str = ''
    reservation_length = ''
    reservation_end_time = ''
    first_name = ''
    last_name = ''
    email = ''
    number_of_guests = ''
    table_location = ''
    table = ''
    message = ''

    # Extract reservation info based on type (object or dictionary)
    if isinstance(reservation, dict):
        reservation_date = reservation.get('reservation_date', '')
        reservation_time = reservation.get('reservation_time', '')
        reservation_length = reservation.get('reservation_length', '')
        reservation_end_time = reservation.get('reservation_end_time', '')
        first_name = reservation.get('first_name', '')
        last_name = reservation.get('last_name', '')
        email = reservation.get('email', '')
        number_of_guests = reservation.get('number_of_guests', '')
        table_location = reservation.get('table_location', '')
        table = reservation.get('table', '')
        message = reservation.get('message', '')
    else:  # Assuming reservation is a Django model object
        reservation_date = reservation.reservation_date
        reservation_time = reservation.reservation_time
        reservation_length = reservation.reservation_length
        reservation_end_time = reservation.reservation_end_time
        first_name = reservation.first_name
        last_name = reservation.last_name
        email = reservation.email
        number_of_guests = reservation.number_of_guests
        table_location = reservation.table_location
        table = reservation.table
        message = reservation.message

    # Similarly handle previous_reservation
    previous_reservation_info = {}
    if previous_reservation:
        if isinstance(previous_reservation, dict):
            previous_reservation_info = previous_reservation
        else:  # Assuming previous_reservation is a Django model object
            previous_reservation_info = {
                'reservation_date': previous_reservation.reservation_date,
                'reservation_time': previous_reservation.reservation_time,
                'reservation_length': previous_reservation.reservation_length,
                'first_name': previous_reservation.first_name,
                'last_name': previous_reservation.last_name,
                'email': previous_reservation.email,
                'number_of_guests': previous_reservation.number_of_guests,
                'table_location': previous_reservation.table_location,
                'table': previous_reservation.table,
                'message': previous_reservation.message,
            }

    if action not in ['create', 'cancel', 'edit']:
        raise ValueError(
            "Invalid action provided. Valid actions"
            "are 'create', 'cancel', 'edit'.")

    if action == 'create':
        subject_guest = 'BigByte - Reservation Confirmation'
        subject_restaurant = 'New Reservation'
    if action == 'cancel':
        subject_guest = 'BigByte - Reservation Cancellation'
        subject_restaurant = 'Reservation Cancelled'
    elif action == 'edit':
        subject_guest = 'BigByte - Reservation Update'
        subject_restaurant = 'Reservation Updated'

    template_guest = f'booking/reservation_{action}_guest.html'
    template_restaurant = f'booking/reservation_{action}_restaurant.html'

    # Format reservation length as "__ hours"
    reservation_length_str = f"{reservation_length} hours"

    # Format reservation time as HH:MM
    reservation_time_str = reservation_time.strftime('%H:%M')
    # reservation_end_time_str = reservation_end_time.strftime('%H:%M')

    # Context for guest and restaurant email
    context_email = {
        'previous_reservation': previous_reservation,
        'reservation': reservation,
    }

    html_message_guest = (
        render_to_string(template_guest, context_email))
    html_message_restaurant = (
        render_to_string(template_restaurant, context_email))

    plain_message_guest = strip_tags(html_message_guest)
    plain_message_restaurant = strip_tags(html_message_restaurant)

    from_email = settings.DEFAULT_FROM_EMAIL
    to_guest = email
    to_restaurant = settings.RESTAURANT_EMAIL

    # Send email to the user
    send_mail(
        subject_guest,
        plain_message_guest,
        from_email,
        [to_guest],
        html_message=html_message_guest)

    # Send email to the restaurant
    send_mail(
        subject_restaurant,
        plain_message_restaurant,
        from_email,
        [to_restaurant],
        html_message=html_message_restaurant)


# Contact form
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

            email_content = render_to_string(
                'booking/contact_restaurant.html', context_email)

            plain_email_content = strip_tags(email_content)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_restaurant = settings.RESTAURANT_EMAIL

            # Send email to the restaurant
            send_mail(
                subject,
                plain_email_content,
                from_email,
                [to_restaurant],
                html_message=email_content)

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


def process_reservation(
        request,
        table_id=None,
        reservation_id=None,
        action='new'):
    if action not in ['new', 'edit']:
        raise ValueError(
            "Invalid action provided. Valid actions are 'new' or 'edit'.")

    reservation = None
    previous_reservation = {}

    # If editing an existing reservation, retrieve it
    if action == 'edit':
        reservation = (
            get_object_or_404(Reservation, reservation_id=reservation_id))
        previous_reservation = {
            'reservation_date': reservation.reservation_date,
            'reservation_time': reservation.reservation_time,
            'reservation_length': reservation.reservation_length,
            'reservation_end_time': reservation.reservation_end_time,
            'first_name': reservation.first_name,
            'last_name': reservation.last_name,
            'number_of_guests': reservation.number_of_guests,
            'table_location': reservation.table_location,
            'table': reservation.table,
            'message': reservation.message,
            'email': reservation.email
        }

    if request.method == 'POST':
        if action == 'new':
            form = ReservationForm(request.POST)
        elif action == 'edit':
            form = EditReservationForm(request.POST, instance=reservation)

        if form.is_valid():
            # Extract cleaned data from the form
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            reservation_length = form.cleaned_data['reservation_length']
            table_location = form.cleaned_data['table_location']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            number_of_guests = form.cleaned_data['number_of_guests']
            message = form.cleaned_data.get('message', '')
            table = table_id

            # Convert time string to datetime object and calculate end time
            if isinstance(reservation_time, str):
                reservation_time = (
                    datetime.strptime(reservation_time, '%H:%M').time())

            reservation_datetime = (
                datetime.combine(reservation_date, reservation_time))
            reservation_end_datetime = (
                reservation_datetime + timedelta(
                    hours=reservation_length) - timedelta(
                        minutes=1))
            reservation_end_time = reservation_end_datetime.time()

            # Set the reservation_end_time before saving the form
            reservation = form.save(commit=False)
            reservation.reservation_end_time = reservation_end_time
            reservation.table_id = table_id

            table = get_object_or_404(RestaurantTable, id=table_id)
            new_table_number = table.table_number

            # If creating a new reservation, save it
            if action == 'new':
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
                send_reservation_email(new_booking, 'create')
                return redirect('thank_you')  # Redirect to thank_you page

            # If editing an existing reservation, update it
            elif action == 'edit':
                updated_reservation = form.save()
                new_reservation_info = {
                    'reservation_date': updated_reservation.reservation_date,
                    'reservation_time': updated_reservation.reservation_time,
                    'reservation_length': (
                        updated_reservation.reservation_length),
                    'first_name': updated_reservation.first_name,
                    'last_name': updated_reservation.last_name,
                    'number_of_guests': updated_reservation.number_of_guests,
                    'table_location': updated_reservation.table_location,
                    'table': new_table_number,
                    'reservation_end_time': reservation_end_time,
                    'message': updated_reservation.message,
                    'email': updated_reservation.email
                }
                send_reservation_email(
                    new_reservation_info,
                    'edit',
                    previous_reservation)
                # Redirect to update_confirmation page
                return redirect('update_confirmed')

    else:
        if action == 'new':
            form = ReservationForm(user=request.user)
        elif action == 'edit':
            form = EditReservationForm(instance=reservation)

    return render(
        request,
        'booking/edit_reservation.html',
        {'form': form, 'reservation': reservation})
