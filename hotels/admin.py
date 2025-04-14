from django.contrib import admin
from .models import Hotel, RoomType, HotelImage, Review

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(HotelImage)
admin.site.register(Review)
