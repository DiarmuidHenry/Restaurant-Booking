# Generated by Django 4.2.12 on 2024-06-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
    ]
