from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MenuItem

def menu_items_list(request):
    # Retrieve all menu items
    menu_items = MenuItem.objects.all()

    # Filtering
    allergens = [
        'contains_gluten', 'contains_crustaceans', 'contains_eggs', 'contains_fish',
        'contains_peanuts', 'contains_soybeans', 'contains_milk', 'contains_nuts',
        'contains_celery', 'contains_mustard', 'contains_sesame', 'contains_sulphur_dioxide_sulphites',
        'contains_lupin', 'contains_molluscs'
    ]

    # Check for allergen filters in query parmaters
    for allergen in allergens:
        if request.GET.get(allergen):
            menu_items = menu_items.filter(**{allergen: False})

    # Check for vegan vegetarian filters
    if request.GET.get('vegan'):
        menu_items = menu_items.filter(vegan=True)
    if request.GET.get('vegetarian'):
        menu_items = menu_items.filter(vegetarian=True)

    # Pagination
    paginator = Paginator(menu_items, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'allergens': allergens
    }

    return render(request, 'allergens/menu_items_list.html', context)