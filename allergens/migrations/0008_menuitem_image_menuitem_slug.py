# Generated by Django 4.2.13 on 2024-07-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0007_alter_menuitem_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
