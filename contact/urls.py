from django.urls import path
from .views import contact, contact_view

urlpatterns = [
     path('', contact_view, name='contact'),
    path('info/', contact_view, name='contact_info'),
]
