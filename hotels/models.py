from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)  # اسم الفندق
    stars = models.IntegerField()  # عدد النجوم
    address = models.TextField()  # العنوان
    details = models.TextField(blank=True, null=True)  # التفاصيل

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE , related_name="room_types")  # الفندق المرتبط بالغرف
    type_name = models.CharField(max_length=50)  # نوع الغرفة (سنجل، دابل، ... إلخ)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # سعر الليلة

    def __str__(self):
        return f"{self.type_name} - {self.hotel.name}"

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # الفندق المرتبط بالصورة
    image = models.ImageField(upload_to='static/images/hotels')  # حفظ الصور في مجلد hotel_images/

    # def __str__(self):
    #      return f"{self.type_name} - {self.hotel.name}"




class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # الفندق المرتبط بالمراجعة
    user_name = models.CharField(max_length=255)  # اسم الشخص اللي كتب الريفيو
    rating = models.IntegerField()  # التقييم (من 1 إلى 5)
    comment = models.TextField()  # التعليق

    def __str__(self):
        return f"Review by {self.user_name} for {self.hotel.name}"



