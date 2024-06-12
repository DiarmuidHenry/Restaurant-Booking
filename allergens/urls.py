from django.urls import path
from .views import test_function

urlpatterns = [
    path('menu/', test_function, name='menu'),
]