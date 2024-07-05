from django.urls import path
from .views import menu_items_list, menu_item_detail

urlpatterns = [
    path('menu/', menu_items_list, name='menu_items_list'),
    path('menu/<slug:slug>/', menu_item_detail, name='menu_item_detail'),
]
