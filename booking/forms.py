from django import forms
from allauth.account.forms import SignupForm
from .models import Reservation
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect, get_object_or_404


# Reservation Form
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['status', 'table', 'reservation_end_time', 'user']

    LENGTH_CHOICES = [
        (1.0, '1 hour'),
        (1.5, '1.5 hours'),
        (2.0, '2 hours'),
        (2.5, '2.5 hours'),
        (3.0, '3 hours'),
    ]

    reservation_length = forms.FloatField(widget=forms.Select(choices=LENGTH_CHOICES))

    # Autofill information from user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

        today = timezone.now().date()
        self.fields['reservation_date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'min': today,
            'max': today + timezone.timedelta(days=365)
        })
        self.fields['reservation_time'].widget = (
            forms.Select(attrs={'required': True}))

        self.fields['reservation_time'].widget = forms.Select(
            choices=[("-", "Please select a date")])

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')
        number_of_guests = cleaned_data.get('number_of_guests')

        if not 1 <= number_of_guests <= 50:
            raise ValidationError("Number of guests must be between 1 and 50.")

        # Format the reservation_time in HH:SS format
        cleaned_data['reservation_time'] = reservation_time.strftime('%H:%M')

        return cleaned_data


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# Contact Form
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(max_length=100, label='Email')
    phone = forms.CharField(max_length=15, label='Phone Number', validators=[
        RegexValidator(
            regex=r'^\+?1?\d{8,15}$',
            message="Invalid Phone Number. Please enter a valid Phone Number.",
        ),
    ])
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))


# Edit Reservation Form
class EditReservationForm(forms.ModelForm):

    LENGTH_CHOICES = [
        (1.0, '1 hour'),
        (1.5, '1.5 hours'),
        (2.0, '2 hours'),
        (2.5, '2.5 hours'),
        (3.0, '3 hours'),
    ]

    reservation_length = forms.FloatField(widget=forms.Select(choices=LENGTH_CHOICES))

    class Meta:
        model = Reservation
        exclude = ['status', 'table', 'reservation_end_time', 'user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditReservationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

        reservation = kwargs.get('instance')
        if reservation:
            initial_length = reservation.reservation_length
            self.fields['reservation_length'].initial = (
                self.format_reservation_length(initial_length))
            if reservation.reservation_time:
                self.fields['reservation_time'].initial = (
                    reservation.reservation_time.strftime('%H:%M'))

        today = timezone.now().date()
        self.fields['reservation_date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'min': today,
            'max': today + timezone.timedelta(days=365)
        })
        self.fields['reservation_time'].widget = (
            forms.Select(attrs={'required': True}))

        self.fields['reservation_time'].widget = forms.Select(
            choices=[("-", "Please select a date")])

    def format_reservation_length(self, length):
        for value, label in self.LENGTH_CHOICES:
            if value == length:
                return label
        return None

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
