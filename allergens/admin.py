from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):

    list_display = ('dish_name', 'section', 'price')
    search_fields = ['dish_name',]
    list_filter = ('section', 'vegetarian', 'vegan',)
    summernote_fields = ()
