# Generated by Django 4.2.12 on 2024-05-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_rename_openingtimes_openinghours'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExceptionalOpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NormalOpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10)),
                ('is_open', models.BooleanField(default=False)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='OpeningHours',
        ),
    ]
