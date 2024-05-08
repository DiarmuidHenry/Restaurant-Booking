from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])