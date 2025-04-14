from django.db import models
from hotels.models import *
from trips.models import *
from trips.models import OneDayTrip

class OneDayTripBooking(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    trip = models.ForeignKey(OneDayTrip, on_delete=models.CASCADE)
    travel_date = models.DateField()
    departure_location = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)

    def remaining_amount(self):
        return self.total_amount - self.paid_amount

    def __str__(self):
        return f"حجز {self.full_name} لـ {self.trip.name}"
    



# هنا سنقوم بتعريف نموذج جديد لحجز الفنادق
class HotelBooking(models.Model):
    ROOM_TYPES = [
        ('single', 'غرفة فردية'),
        ('double', 'غرفة مزدوجة'),
        ('suite', 'جناح'),
    ]

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    nights = models.PositiveIntegerField()
    internal_trips = models.ManyToManyField(InternalTrip, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    departure_location = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    def remaining_amount(self):
        return self.total_amount - self.paid_amount
    def __str__(self):
        return f"حجز {self.full_name} في {self.hotel.name}"






class Package(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الباكدج")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="الفندق")
    trips = models.ManyToManyField(InternalTrip, blank=True, verbose_name="الرحلات الداخلية")
    duration_nights = models.IntegerField(default=3, verbose_name="عدد الليالي")
    duration_days = models.IntegerField(default=4, verbose_name="عدد الأيام")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر للفردين")

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"

    def get_trip_names(self):
        return ", ".join([trip.name for trip in self.trips.all()])





class PackageBooking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)  # الباكدج المحجوز
    full_name = models.CharField(max_length=255)  # الاسم الكامل
    phone_number = models.CharField(max_length=20)  # رقم الهاتف
    travel_date = models.DateField()  # تاريخ السفر
    return_date = models.DateField()  # تاريخ العودة
    pickup_location = models.CharField(max_length=255)  # مكان التحرك
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # السعر الإجمالي
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)  # المدفوع
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)  # المتبقي
    booking_date = models.DateTimeField(auto_now_add=True)  # تاريخ الحجز تلقائي

    def __str__(self):
        return f"حجز {self.full_name} لـ {self.package.name}"

