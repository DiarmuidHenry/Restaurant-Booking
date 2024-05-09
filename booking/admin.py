from django.contrib import admin
from .models import RestaurantTable
from .models import Reservation

# Register your models here.
admin.site.register(RestaurantTable)
admin.site.register(Reservation)