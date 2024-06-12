from django.db import models

# Create your models here.
class MenuItem(models.Model):
    dish_name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    contains_gluten = models.BooleanField(default=False)
    contains_crustaceans = models.BooleanField(default=False)
    contains_eggs = models.BooleanField(default=False)
    contains_fish = models.BooleanField(default=False)
    contains_peanuts = models.BooleanField(default=False)
    contains_soy = models.BooleanField(default=False)
    contains_dairy = models.BooleanField(default=False)
    contains_nuts = models.BooleanField(default=False)
    contains_celery = models.BooleanField(default=False)
    contains_mustard = models.BooleanField(default=False)
    contains_sesame = models.BooleanField(default=False)
    contains_sulphur_dioxide_sulphites = models.BooleanField(default=False)
    contains_lupin = models.BooleanField(default=False)
    contains_molluscs = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.dish_name