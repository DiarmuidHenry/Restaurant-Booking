from django.contrib import admin
from .models import RestaurantTable
from .models import Reservation
from .models import NormalOpeningHours
from .models import ExceptionalOpeningHours

# Register your models here.
admin.site.register(RestaurantTable)
admin.site.register(Reservation)
admin.site.register(NormalOpeningHours)
admin.site.register(ExceptionalOpeningHours)