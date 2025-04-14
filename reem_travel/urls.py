from django.contrib import admin
from django.urls import path , include
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  # الصفحة الرئيسية
    path('hotels/', include('hotels.urls')),  # الفنادق
    path('trips/', include('trips.urls')),  # الرحلات
    path('bookings/', include('bookings.urls')),  # الحجوزات
    path('contact/', include('contact.urls')),  # التواصل
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


