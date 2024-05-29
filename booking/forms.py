from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['status', 'table']

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')

        # Format the reservation_time in HH:SS format
        cleaned_data['reservation_time'] = reservation_time.strftime('%H:%S')

        return cleaned_data