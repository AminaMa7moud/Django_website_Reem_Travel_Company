from django.urls import path
from .views import *

urlpatterns = [
    path('', hotel_list, name='hotel_list'),
    path('<int:hotel_id>/', hotel_detail, name='hotel_detail'),
]
