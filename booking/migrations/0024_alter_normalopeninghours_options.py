# Generated by Django 4.2.13 on 2024-07-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_alter_reservation_number_of_guests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normalopeninghours',
            options={'ordering': ['day']},
        ),
    ]