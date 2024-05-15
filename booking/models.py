from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

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


class ExceptionalOpeningHours(models.Model):
    date = models.DateField(unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def clean(self):
        from datetime import datetime

        now = datetime.now()

        # Check if entered date is in the future
        if self.date <= now.date():
            raise ValidationError("Exceptional opening hours can only be created for future dates.")


class RestaurantTable(models.Model):
    LOCATION_CHOICES = [
        ('inside', 'Inside'),
        ('outside', 'Outside'),
    ]

    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default=0)

class Reservation(models.Model):
    LOCATION_CHOICES = [
        ('inside', 'Inside'),
        ('outside', 'Outside'),
    ]

    STATUS_CHOICES = [
        (1, 'Confirmed'),
        (0, 'Cancelled'),
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
    reservation_length = models.CharField(choices=LENGTH_CHOICES, default=2)
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_location = models.CharField(choices=LOCATION_CHOICES, default=0)
    status = models.CharField(choices=STATUS_CHOICES, default=1)

    def clean(self):
        from datetime import datetime, timedelta
        from dateutil.relativedelta import relativedelta

        now = datetime.now()

        # Calculate reservation end time based on start time and length
        reservation_end_time = datetime.combine(self.reservation_date, self.reservation_time) + timedelta(hours=float(self.reservation_length))

        # Get opening times for the reservation date, first checking ExceptionalOpeningHours
        reservation_day_opening_hours = None
        try:
            # Check if there are exceptional opening hours for the reservation date
            exceptional_opening_hours = ExceptionalOpeningHours.objects.get(date=self.reservation_date)
            reservation_day_opening_hours = exceptional_opening_hours
        except ExceptionalOpeningHours.DoesNotExist:
            # If no exceptional opening hours, use regular opening hours
            try:
                # Use regular opening hours for the reservation date
                regular_opening_hours = RegularOpeningHours.objects.get(day=self.reservation_date.strftime('%A').lower())
                reservation_day_opening_hours = regular_opening_hours
            except RegularOpeningHours.DoesNotExist:
                # If no opening hours are defined for the reservation date
                pass

        # Check if requested reservation date is in the past
        if self.reservation_date < now.date():
            raise ValidationError("Reservation date cannot be in the past.")

        # Check if reservation for today is in past on current day
        if self.reservation_date == now.date() and self.reservation_time <= now.time():
            raise ValidationError("Reservation time cannot be in the past on the current day.")
        
        # Check if requested reservation ends after closing time on that day
        if reservation_end_time > reservation_day_close:
            raise ValidationError(f"The requested reservation ends after closing time for {self.reservation_date.strftime('%A')} {self.reservation_date}. Please choose an earlier reservation time, or a shorter reservation length.")

        # Check if requested reservation date is more than 1 year in the future
        if reservation_date > (now.date() + relativedelta(years=1)):
            raise ValidationError("Reservations can only be made up to 1 year in advance.")