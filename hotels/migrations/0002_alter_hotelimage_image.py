# Generated by Django 5.1.6 on 2025-03-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelimage',
            name='image',
            field=models.ImageField(upload_to='images/hotels/'),
        ),
    ]
