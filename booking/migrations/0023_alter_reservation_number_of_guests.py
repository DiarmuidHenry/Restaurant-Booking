# Generated by Django 4.2.13 on 2024-07-11 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_reservation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_guests',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
