from django import forms
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationView(FormView):
    template_name = 'booking/booking_form.html'
    form_class = ReservationForm
    success_url = '/thank_you/'

    def form_valid(self, form):
        print("Form is valid")
        form.save()
        return super().form_valid(form)

def thank_you(request):
    return render(request, 'booking/thank_you.html')

def home(request):
    return render(request, 'booking/home.html')