from .models import NormalOpeningHours

# Check and load correct opening hours in footer upon refresh
def opening_hours(request):
    opening_hours = NormalOpeningHours.objects.all()
    return {'opening_hours': opening_hours}