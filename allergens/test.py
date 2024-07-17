from django.test import TestCase
from allergens.models import MenuItem
from django.urls import reverse

class MenuItemList(TestCase):
    # Create example menu items!
    def setUp(self):
        MenuItem.objects.create(
            dish_name = "Dish 1",
            description = "Dish 1 description",
            section = "mains",
            price = "1",
            gluten = False,
            crustaceans = False,
            eggs = False,
            fish = False,
            peanuts = False,
            soy = False,
            dairy = False,
            nuts = False,
            celery = False,
            mustard = False,
            sesame = False,
            sulphites = False,
            lupin = False,
            molluscs = False,
            vegan = False,
            vegetarian = False,
            slug = "dish_1"
        )
        MenuItem.objects.create(
            dish_name = "Dish 2",
            description = "Dish 2 description",
            section = "mains",
            price = "1",
            gluten = False,
            crustaceans = False,
            eggs = False,
            fish = False,
            peanuts = False,
            soy = False,
            dairy = False,
            nuts = False,
            celery = False,
            mustard = False,
            sesame = False,
            sulphites = False,
            lupin = False,
            molluscs = False,
            vegan = True,
            vegetarian = True,
            slug = "dish_2"
        )
        MenuItem.objects.create(
            dish_name = "Dish 3",
            description = "Dish 3 description",
            section = "mains",
            price = "1",
            gluten = False,
            crustaceans = False,
            eggs = False,
            fish = False,
            peanuts = False,
            soy = False,
            dairy = False,
            nuts = False,
            celery = False,
            mustard = False,
            sesame = False,
            sulphites = False,
            lupin = False,
            molluscs = False,
            vegan = False,
            vegetarian = True,
            slug = "dish_3"
        )
        MenuItem.objects.create(
            dish_name = "Dish 4",
            description = "Dish 4 description",
            section = "mains",
            price = "1",
            gluten = True,
            crustaceans = False,
            eggs = False,
            fish = False,
            peanuts = False,
            soy = False,
            dairy = False,
            nuts = False,
            celery = False,
            mustard = False,
            sesame = False,
            sulphites = False,
            lupin = False,
            molluscs = False,
            vegan = True,
            vegetarian = True,
            slug = "dish_4"
        )
        MenuItem.objects.create(
            dish_name = "Dish 5",
            description = "Dish 5 description",
            section = "mains",
            price = "1",
            gluten = True,
            crustaceans = False,
            eggs = False,
            fish = False,
            peanuts = False,
            soy = False,
            dairy = False,
            nuts = False,
            celery = False,
            mustard = False,
            sesame = False,
            sulphites = False,
            lupin = False,
            molluscs = False,
            vegan = False,
            vegetarian = True,
            slug = "dish_5"
        )

    def test_menu_items_list_view(self):
        # Test the entire view behavior including pagination and section filtering

        # Make GET request to menu_items_list view
        response = self.client.get(reverse('menu_items_list'))
        self.assertEqual(response.status_code, 200)

        # Check that all menu items are present in the response
        self.assertTrue('page_obj' in response.context)
        page_obj = response.context['page_obj']
        self.assertEqual(page_obj.paginator.count, MenuItem.objects.count())

        # Test section filtering (example: mains)
        response = self.client.get(reverse('menu_items_list') + '?section=mains')
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        self.assertTrue(all(item.section == 'mains' for item in page_obj))

    def test_allergen_ticked_filtering(self):
        # Test allergen filtering
        
        # Test gluten=True filtering
        response = self.client.get(reverse('menu_items_list') + '?gluten=true')
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        self.assertFalse(all(item.gluten for item in page_obj))

    def test_allergen_not_ticked_filtering(self):
        # Test that filtering with gluten=false does not affect the response
        response = self.client.get(reverse('menu_items_list'))
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        # Check that there are items with gluten=False and gluten=True in the response
        self.assertTrue(any(item.gluten for item in page_obj))  # Check for gluten=True items
        self.assertTrue(any(not item.gluten for item in page_obj))  # Check for gluten=False items

    def test_dietary_requirement_ticked_filtering(self):
        # Test vegan filtering
        
        # Test vegan=True filtering
        response = self.client.get(reverse('menu_items_list') + '?vegan=true')
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        self.assertTrue(all(item.vegan for item in page_obj))

    def test_dietary_requirement_not_ticked_filtering(self):
        # Test that filtering with vegann=false does not affect the response
        response = self.client.get(reverse('menu_items_list'))
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        # Check that there are items with vegan=False and vegan=True in the response
        self.assertTrue(any(item.vegan for item in page_obj))  # Check for gluten=True items
        self.assertTrue(any(not item.vegan for item in page_obj))  # Check for gluten=False items
