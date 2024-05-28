from django import forms
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationView(FormView):
    template_name = 'booking/booking_form.html'
    form_class = ReservationForm
    success_url = '/thank-you/'

    def form_valid(self, form):
        print("Form is valid")
        form.save()
        return super().form_valid(form)
