# Generated by Django 5.1.6 on 2025-03-06 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternalTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('price_per_person', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OneDayTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('price_per_person', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trip_images/')),
                ('one_day_trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.onedaytrip')),
                ('trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.internaltrip')),
            ],
        ),
    ]
