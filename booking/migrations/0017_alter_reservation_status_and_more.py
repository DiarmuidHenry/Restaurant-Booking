# Generated by Django 4.2.13 on 2024-07-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_reservation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table_location',
            field=models.CharField(choices=[('Inside', 'Inside'), ('Outside', 'Outside')], default='inside', max_length=50),
        ),
        migrations.AlterField(
            model_name='restauranttable',
            name='table_location',
            field=models.CharField(choices=[('Inside', 'Inside'), ('Outside', 'Outside')], default='inside', max_length=50),
        ),
    ]