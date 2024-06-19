from django import forms
from allauth.account.forms import SignupForm
from .models import Reservation
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['status', 'table', 'reservation_end_time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

        today = timezone.now().date()
        self.fields['reservation_date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'min': today,
            'max': today + timezone.timedelta(days=365)
        })
        self.fields['reservation_time'].widget = forms.Select()

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')
        number_of_guests = cleaned_data.get('number_of_guests')

        # if reservation_time is None:
        #     raise forms.ValidationError("Reservation time is required.")
        # if number_of_guests is None:
        #     raise forms.ValidationError("Number of guests is required.")

        # Format the reservation_time in HH:SS format
        cleaned_data['reservation_time'] = reservation_time.strftime('%H:%S')

        return cleaned_data

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        return user