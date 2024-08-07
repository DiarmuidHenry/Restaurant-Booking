from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
import os
import shutil
from django.conf import settings
from django.conf.urls.static import static

# Menu item description and allergen information
class MenuItem(models.Model):
    SECTION_CHOICES = [
        ('starters', 'Starters'),
        ('mains', 'Mains'),
        ('sides', 'Sides'),
        ('kids', 'Kids'),
        ('desserts', 'Desserts'),
    ]

    dish_name = models.TextField()
    description = models.TextField()
    section = models.CharField(
        choices=SECTION_CHOICES, default='mains', max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
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
    image = CloudinaryField('image', null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.dish_name} | {self.section}"

    # Automatic slug creation for more readable url
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.dish_name)

        super().save(*args, **kwargs)
