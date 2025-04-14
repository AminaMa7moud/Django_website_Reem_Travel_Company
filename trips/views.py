from django.shortcuts import render, get_object_or_404
from .models import InternalTrip, OneDayTrip

def trip_list(request):
    trip_type = request.GET.get('type', 'one_day')  

    if trip_type == 'internal':
        trips = InternalTrip.objects.all()
        title = ' رحلات فى شرم'
        type_value = 'internal'
    else:
        trips = OneDayTrip.objects.all()
        title = 'رحلات اليوم الواحد'
        type_value = 'one_day'

    context = {
        'trips': trips,
        'trip_type': trip_type,
        'title': title,
        'type_value': type_value
    }
    return render(request, 'trips/trip_list.html', context)

def internal_trip_detail(request, trip_id):
    trip = get_object_or_404(InternalTrip, id=trip_id)
    return render(request, 'trips/trip_detail.html', {'trip': trip})

def one_day_trip_detail(request, trip_id):
    trip = get_object_or_404(OneDayTrip, id=trip_id)
    return render(request, 'trips/trip_detail.html', {'trip': trip})
