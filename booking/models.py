from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

class Reservation(models.Model):
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
    status = models.CharField(choices=STATUS_CHOICES, default=1)