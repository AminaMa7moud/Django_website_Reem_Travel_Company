from django.urls import path
from .views import *
urlpatterns = [
    path('', trip_list, name='trip_list'),
    path('internal/<int:trip_id>/', internal_trip_detail, name="internal_trip_detail"),
    path('one_day/<int:trip_id>/', one_day_trip_detail, name="one_day_trip_detail"),
]
