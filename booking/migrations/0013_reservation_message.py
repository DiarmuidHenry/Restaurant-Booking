# Generated by Django 4.2.12 on 2024-06-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_reservation_reservation_end_time_delete_tablebooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='message',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
