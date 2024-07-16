from .models import NormalOpeningHours

def opening_hours(request):
    opening_hours = NormalOpeningHours.objects.all()
    return {'opening_hours': opening_hours}