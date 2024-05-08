from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

class Reservation(models.Model):
    STATUS_CHOICES = [
        (1, 'Confirmed'),
        (0, 'Canceled'),
    ]

    reservation_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(default=timezone.now)
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=1)