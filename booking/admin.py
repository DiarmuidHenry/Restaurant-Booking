from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    RestaurantTable,
    Reservation,
    NormalOpeningHours,
    ExceptionalOpeningHours
)


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = (
        'first_name', 'last_name', 'reservation_date',
        'reservation_time', 'reservation_end_time', 'reservation_id')
    search_fields = ['reservation_id', 'first_name', 'last_name']
    list_filter = ('created_on', 'reservation_date',)
    summernote_fields = ('reservation_id',)
    exclude = ('reservation_length',)

@admin.register(RestaurantTable)
class RestaurantTableAdmin(SummernoteModelAdmin):

    list_display = (
        'table_number', 'capacity', 'table_location',)
    search_fields = ['table_number', 'location',]
    list_filter = ('capacity', 'table_location',)


# Register your models here.
admin.site.register(NormalOpeningHours)
admin.site.register(ExceptionalOpeningHours)
