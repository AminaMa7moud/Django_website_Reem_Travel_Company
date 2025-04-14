from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class InternalTrip(models.Model):
    name = models.CharField(max_length=255)  # اسم الرحلة
    details = models.TextField()  # التفاصيل
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)  # سعر الفرد

    def __str__(self):
        return self.name

class OneDayTrip(models.Model):
    name = models.CharField(max_length=255)  # اسم الرحلة
    location = models.CharField(max_length=255)  # المكان
    details = models.TextField()  # التفاصيل
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)  # سعر الفرد

    def __str__(self):
        return self.name


# جدول صور الرحلات الداخلية
class InternalTripImage(models.Model):
    trip = models.ForeignKey(InternalTrip, on_delete=models.CASCADE, related_name="images")  
    image = models.ImageField(upload_to='static/images/internal_trips/')  # حفظ الصور في مجلد منفصل
    def __str__(self):
        return f"Image for {self.trip.name}"


# جدول صور رحلات اليوم الواحد
class OneDayTripImage(models.Model):
    trip = models.ForeignKey(OneDayTrip, on_delete=models.CASCADE, related_name="images")  
    image = models.ImageField(upload_to='static/images/one_day_trips/')  # حفظ الصور في مجلد منفصل
    def __str__(self):
        return f"Image for {self.trip.name}"