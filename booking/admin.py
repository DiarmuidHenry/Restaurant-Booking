from django.contrib import admin
from .models import RestaurantTable, Reservation, NormalOpeningHours, ExceptionalOpeningHours

# Register your models here.
admin.site.register(RestaurantTable)
admin.site.register(Reservation)
admin.site.register(NormalOpeningHours)
admin.site.register(ExceptionalOpeningHours)