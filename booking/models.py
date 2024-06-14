from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta, time
import time
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

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
        ('inside', 'Inside'),
        ('outside', 'Outside'),
    ]

    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default=0)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"Table {self.table_number} | Capacity: {self.capacity} | {self.table_location}"

    
class Reservation(models.Model):
    LOCATION_CHOICES = [
        ('inside', 'Inside'),
        ('outside', 'Outside'),
    ]

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    LENGTH_CHOICES = [
        (1, '1 hour'),
        (1.5, '1.5 hours'),
        (2, '2 hours'),
        (2.5, '2.5 hours'),
        (3, '3 hours'),
    ]

    reservation_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateField(default=timezone.now)
    reservation_time = models.TimeField(default=timezone.now)
    reservation_length = models.FloatField(choices=LENGTH_CHOICES, default=2)
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default='inside')
    status = models.CharField(choices=STATUS_CHOICES, default=1)
    reservation_end_time = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate reservation end time before saving
        reservation_start_datetime = datetime.combine(self.reservation_date, self.reservation_time)
        reservation_end_datetime = reservation_start_datetime + timedelta(hours=self.reservation_length)
        self.reservation_end_time = reservation_end_datetime.time()
        super().save(*args, **kwargs)

    # def formatted_reservation_time(self):
    #     return self.reservation_time.strftime('%H:%S')

    # def set_formatted_reservation_time(self, value):
    #     # Parse the value in HH:SS format and set it to reservation_time
    #     self.reservation_time = datetime.strptime(value, '%H:%S').time()

    def clean(self):

        if self.number_of_guests is None:
            raise ValidationError("Number of guests is required.")

        print(f"Reservation Date: {self.reservation_date}")
        print(f"Reservation Time: {self.reservation_time}")
        print(f"Reservation Length: {self.reservation_length}")

        if self.number_of_guests > 8:
            raise ValidationError(f"If you wish to make a reservation for {self.number_of_guests} people, please email the restaurant directly and we will do our best to accommodate you. INSERT EMAIL LINK HERE?!")
    
        now = datetime.now()

        # Calculate reservation start and end datetime based on start time and length
        reservation_start_datetime = datetime.combine(self.reservation_date, self.reservation_time)
        reservation_start_time = reservation_start_datetime.time()
        reservation_end_datetime = reservation_start_datetime + timedelta(hours=self.reservation_length)
        reservation_end_time = reservation_end_datetime.time()
        print("reservation_start_datetime : ", reservation_start_datetime)
        print("reservation_start_time :", reservation_start_time)
        print("reservation_end_datetime : ", reservation_end_datetime)
        print("reservation_end_time : ", reservation_end_time)
        
        # Get opening times for the reservation date, first checking ExceptionalOpeningHours
        reservation_day_open = None
        reservation_day_close = None
        try:
            exceptional_opening_hours = ExceptionalOpeningHours.objects.get(date=self.reservation_date)
            if exceptional_opening_hours.is_open:
                reservation_day_open = exceptional_opening_hours.opening_time
                reservation_day_close = exceptional_opening_hours.closing_time
                print(f"Exceptional Opening Hours: {reservation_day_open} - {reservation_day_close}")
            else:
                print("No exceptional opening hours exist")
                raise ValidationError("The restaurant is closed on the selected date.")
        except ExceptionalOpeningHours.DoesNotExist:
            # If no exceptional opening hours, use nromal opening hours
            try:
                # Use normal opening hours for the reservation date
                normal_opening_hours = NormalOpeningHours.objects.get(day=self.reservation_date.strftime('%A').lower())
                if not normal_opening_hours.is_open:
                    print("Normal opening hours says restaurant is closed")
                    raise ValidationError(f"The restaurant is closed on {self.reservation_date.strftime('%A')}s.")
                reservation_day_open = normal_opening_hours.opening_time
                reservation_day_open_datetime = datetime.combine(self.reservation_date, reservation_day_open)
                reservation_day_close = normal_opening_hours.closing_time
                reservation_day_close_datetime = datetime.combine(self.reservation_date, reservation_day_close)

                print(f"Normal Opening Hours: {reservation_day_open} - {reservation_day_close}")
            except NormalOpeningHours.DoesNotExist:
                # If no opening hours are defined for the reservation date, raise an error
                raise ValidationError("No opening hours are defined for the selected reservation date.")

        print("Reservation_day_open :", reservation_day_open)
        print("Reservation_day_close :", reservation_day_close)
        print("Reservation_day_close_datetime :", reservation_day_close_datetime)
        print("Reservation day close type :", type(reservation_day_close))
        print("Reservation_start_time type :", type(reservation_start_time))
        print("Reservation_day_close_datetime type :", type(reservation_day_close_datetime))
        # Check if requested reservation date is in the past
        if self.reservation_date < now.date() or (self.reservation_date == now.date() and self.reservation_time <= now.time()):
            raise ValidationError("Reservation date cannot be in the past.")

        # Check if requested reservation starts before opening time on that day
        if reservation_start_datetime < reservation_day_open_datetime:
            raise ValidationError(f"The requested reservation begins before opening time ({reservation_day_open}) for {self.reservation_date.strftime('%A')} {self.reservation_date}. Please choose a later reservation time.")
        
        # Check if requested reservation ends after closing time on that day
        if reservation_start_datetime > (reservation_day_close_datetime - timedelta(hours=self.reservation_length)):
            raise ValidationError(f"The requested reservation ends after closing time ({reservation_day_close}) for {self.reservation_date.strftime('%A')} {self.reservation_date}. Please choose an earlier reservation time, or a shorter reservation length.")

        # Check if requested reservation date is more than 1 year in the future
        if self.reservation_date > (now.date() + timedelta(days=365)):
            raise ValidationError("Reservations can only be made up to 1 year in advance.")

    class Meta:
        ordering = ["reservation_date"]

    def __str__(self):
        return f"{self.reservation_date} - {self.reservation_time} | {self.customer_name} | {self.number_of_guests}"

    