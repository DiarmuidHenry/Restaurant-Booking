from django.db import models
from django.core.validators import MinValueValidator, ValidationError
from django.utils import timezone
from datetime import timedelta
from datetime import datetime
from django.contrib.auth.models import User
from allergens.models import MenuItem
from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your models here.

class NormalOpeningHours(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    is_open = models.BooleanField(default=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def clean(self):
        # Check that opening_time is before closing_time
        if self.is_open and self.opening_time and self.closing_time:
            if self.opening_time >= self.closing_time:
                raise ValidationError("Closing time must be later than opening time.")

    def __str__(self):
        if self.is_open:
            return f"{self.day} | {self.opening_time} - {self.closing_time}"
        else:
            return f"{self.day} - CLOSED"

class ExceptionalOpeningHours(models.Model):
    date = models.DateField(unique=True)
    is_open = models.BooleanField(default=False)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    def clean(self):
        from datetime import datetime

        now = datetime.now()

        # Check if entered date is in the future
        if self.date <= now.date():
            raise ValidationError("Exceptional opening hours can only be created for future dates.")
        
        # Check if opening_time and closing_time exist, when is_open is True
        if self.is_open:
            if not self.opening_time or not self.closing_time:
                raise ValidationError("Opening and closing times must be set if the restaurant is open.")
            if self.opening_time >= self.closing_time:
                raise ValidationError("Closing time must be later than opening time.")
        else:
            self.opening_time = None
            self.closing_time = None

    class Meta:
        ordering = ["date"]

    def __str__(self):
        if self.is_open:
            return f"{self.date} | {self.opening_time} - {self.closing_time}"
        else:
            return f"{self.date} - CLOSED" 

class RestaurantTable(models.Model):
    LOCATION_CHOICES = [
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
    ]

    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default='Inside', max_length=50)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"{self.table_number}"

class Reservation(models.Model):
    LOCATION_CHOICES = [
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
    ]

    LENGTH_CHOICES = [
        (1, '1 hour'),
        (1.5, '1.5 hours'),
        (2, '2 hours'),
        (2.5, '2.5 hours'),
        (3, '3 hours'),
    ]

    def validate_reservation_time(value):
        if value is None:
            raise ValidationError('Reservation time cannot be empty.')

    reservation_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, default='')
    last_name = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateField()
    reservation_length = models.FloatField(choices=LENGTH_CHOICES, default=2)
    reservation_time = models.TimeField(blank=False)
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default='Inside', max_length=50)
    reservation_end_time = models.TimeField(null=True, blank=True)
    message = models.TextField(max_length=200, blank=True, null=True) 

    def formatted_reservation_time(self):
        return self.reservation_time.strftime('%H:%M')

    def formatted_reservation_end_time(self):
        return self.reservation_end_time.strftime('%H:%M')

    def reservation_end_time_plus_one_minute(self):
        end_datetime = datetime.combine(self.reservation_date, self.reservation_end_time)
        end_datetime_plus_one_minute = end_datetime + timedelta(minutes=1)
        return end_datetime_plus_one_minute.strftime('%H:%M')

    def clean(self):
        if self.number_of_guests is None:
            raise ValidationError("Number of guests is required.")

        if self.reservation_time is None:
            raise ValidationError("Reservation time is required.")

    class Meta:
        ordering = ["reservation_date"]
