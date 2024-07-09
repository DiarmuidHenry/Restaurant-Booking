from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import MenuItem

def menu_items_list(request):
    # Retrieve all menu items
    menu_items = MenuItem.objects.all()

    # Filtering
    allergens = [
        'Gluten', 'Crustaceans', 'Eggs', 'Fish',
        'Peanuts', 'Soy', 'Dairy', 'Nuts',
        'Celery', 'Mustard', 'Sesame', 'Sulphites',
        'Lupin', 'Molluscs'
    ]

    # Check for allergen filters in query parmaters
    for allergen in allergens:
        if request.GET.get(allergen):
            allergen = allergen.lower()
            menu_items = menu_items.filter(**{allergen: False})

    # Check for vegan vegetarian filters
    if request.GET.get('vegan'):
        menu_items = menu_items.filter(vegan=True)
    if request.GET.get('vegetarian'):
        menu_items = menu_items.filter(vegetarian=True)

    # Pagination
    paginator = Paginator(menu_items, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    starters = menu_items.filter(section='starters')
    mains = menu_items.filter(section='mains')
    kids = menu_items.filter(section='kids')
    sides = menu_items.filter(section='sides')
    desserts = menu_items.filter(section='desserts')

    context = {
        'page_obj': page_obj,
        'allergens': allergens,
        'starters': starters,
        'mains': mains,
        'kids': kids,
        'sides': sides,
        'desserts': desserts,
    }

    return render(request, 'allergens/menu_items_list.html', context)


def menu_item_detail(request, slug):
    item = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'allergens/menu_item_detail.html', {'item': item})