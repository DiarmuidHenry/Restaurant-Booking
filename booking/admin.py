from django.contrib import admin
from .models import RestaurantTable, Reservation, NormalOpeningHours, ExceptionalOpeningHours
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('reservation_id', 'reservation_date', 'reservation_time')
    search_fields = ['reservation_id', 'customer_name',]
    list_filter = ('status', 'created_on', 'reservation_date',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('reservation_id',)

# Register your models here.
admin.site.register(RestaurantTable)
admin.site.register(NormalOpeningHours)
admin.site.register(ExceptionalOpeningHours)