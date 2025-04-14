# Generated by Django 5.1.6 on 2025-04-14 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_packagebooking'),
        ('hotels', '0004_alter_roomtype_hotel'),
        ('trips', '0004_internaltripimage_onedaytripimage_delete_tripimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='duration_days',
            field=models.IntegerField(default=4, verbose_name='عدد الأيام'),
        ),
        migrations.AlterField(
            model_name='package',
            name='duration_nights',
            field=models.IntegerField(default=3, verbose_name='عدد الليالي'),
        ),
        migrations.AlterField(
            model_name='package',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel', verbose_name='الفندق'),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=255, verbose_name='اسم الباكدج'),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر للفردين'),
        ),
        migrations.AlterField(
            model_name='package',
            name='trips',
            field=models.ManyToManyField(blank=True, to='trips.internaltrip', verbose_name='الرحلات الداخلية'),
        ),
    ]
