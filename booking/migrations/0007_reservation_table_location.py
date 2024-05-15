# Generated by Django 4.2.12 on 2024-05-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_restauranttable_table_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table_location',
            field=models.CharField(choices=[(0, 'Inside'), (1, 'Outside')], default=0),
        ),
    ]
