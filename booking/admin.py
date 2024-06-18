from django.contrib import admin
from .models import RestaurantTable, Reservation, NormalOpeningHours, ExceptionalOpeningHours
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'phone_number', 'reservation_date', 'reservation_time', 'reservation_end_time', 'reservation_id')
    search_fields = ['reservation_id', 'n,ame',]
    list_filter = ('status', 'created_on', 'reservation_date',)
    summernote_fields = ('reservation_id',)

# Register your models here.
admin.site.register(RestaurantTable)
admin.site.register(NormalOpeningHours)
admin.site.register(ExceptionalOpeningHours)