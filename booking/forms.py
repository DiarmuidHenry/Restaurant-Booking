from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['status', 'table', 'reservation_end_time']

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')
        number_of_guests = cleaned_data.get('number_of_guests')

        if reservation_time is None:
            raise forms.ValidationError("Reservation time is required.")
        if number_of_guests is None:
            raise forms.ValidationError("Number of guests is required.")

        # Format the reservation_time in HH:SS format
        cleaned_data['reservation_time'] = reservation_time.strftime('%H:%S')

        return cleaned_data