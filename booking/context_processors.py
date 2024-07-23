from .models import NormalOpeningHours
from django.db.models import Case, When, Value, IntegerField


def opening_hours(request):
    order = Case(
        When(day='monday', then=Value(1)),
        When(day='tuesday', then=Value(2)),
        When(day='wednesday', then=Value(3)),
        When(day='thursday', then=Value(4)),
        When(day='friday', then=Value(5)),
        When(day='saturday', then=Value(6)),
        When(day='sunday', then=Value(7)),
        output_field=IntegerField(),
    )
    opening_hours = NormalOpeningHours.objects.all().order_by(order)
    return {'opening_hours': opening_hours}
