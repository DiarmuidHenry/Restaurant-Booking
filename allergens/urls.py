from django.urls import path
from .views import menu_items_list

urlpatterns = [
    path('menu/', menu_items_list, name='menu_items_list'),
]