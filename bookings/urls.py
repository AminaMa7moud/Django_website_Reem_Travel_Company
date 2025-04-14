from django.urls import path
from .views import *
urlpatterns = [
    path('', booking_home, name='booking_home'),
    path('one-day-trip/', book_one_day_trip, name='book_one_day_trip'),
    path('hotel/', book_hotel, name='book_hotel'),
    path('packages/', packages_list, name='packages_list'),
    path('packages/<int:package_id>/', package_detail, name='package_detail'),
    path('packages/<int:package_id>/book/', book_package, name='book_package'),
    path('booking-success/', booking_success, name='booking_success'),

]
