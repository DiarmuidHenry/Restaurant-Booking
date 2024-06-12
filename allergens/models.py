from django.db import models

# Create your models here.
class MenuItem(models.Model):
    dish_name = models.TextField()
    description = models.TextField()
    gluten = models.BooleanField(default=False)
    crustaceans = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    fish = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    dairy = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    celery = models.BooleanField(default=False)
    mustard = models.BooleanField(default=False)
    sesame = models.BooleanField(default=False)
    sulphites = models.BooleanField(default=False)
    lupin = models.BooleanField(default=False)
    molluscs = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    # def clean(self):


    def __str__(self):
        return self.dish_name