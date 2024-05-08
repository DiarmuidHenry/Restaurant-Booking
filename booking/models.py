from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RestaurantTable(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()