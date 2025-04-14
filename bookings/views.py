from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from trips.models import OneDayTrip , InternalTrip
from hotels.models import Hotel
from .forms import PackageBookingForm


def booking_home(request):
    return render(request, 'booking/booking_home.html')

def book_one_day_trip(request):
    return render(request, 'booking/book_one_day_trip.html')

def book_hotel(request):
    return render(request, 'booking/book_hotel.html')



def book_one_day_trip(request):
    trips = OneDayTrip.objects.all()
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        trip = OneDayTrip.objects.get(id=request.POST['trip'])
        travel_date = request.POST['travel_date']
        departure_location = request.POST['departure_location']
        total_amount = request.POST['total_amount']
        paid_amount = request.POST['paid_amount']
        OneDayTripBooking.objects.create(
            full_name=full_name,
            phone=phone,
            trip=trip,
            travel_date=travel_date,
            departure_location=departure_location,
            total_amount=total_amount,
            paid_amount=paid_amount
        )
        return redirect('booking_home')
    return render(request, 'booking/book_one_day_trip.html', {'trips': trips})







def book_hotel(request):
    hotels = Hotel.objects.all()
    internal_trips = InternalTrip.objects.all()

    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        hotel = Hotel.objects.get(id=request.POST['hotel'])
        room_type = request.POST['room_type']
        nights = request.POST['nights']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        departure_location = request.POST['departure_location']
        total_amount = request.POST['total_amount']
        paid_amount = request.POST['paid_amount']
        booking = HotelBooking.objects.create(
            full_name=full_name,
            phone=phone,
            hotel=hotel,
            room_type=room_type,
            nights=nights,
            check_in=check_in,
            check_out=check_out,
            departure_location=departure_location,
            total_amount=total_amount,
            paid_amount=paid_amount
        )
        selected_trips = request.POST.getlist('internal_trips')
        for trip_id in selected_trips:
            trip = InternalTrip.objects.get(id=trip_id)
            booking.internal_trips.add(trip)
        return redirect('booking_home')
    return render(request, 'booking/book_hotel.html', {'hotels': hotels, 'internal_trips': internal_trips})




def packages_list(request):
    packages = Package.objects.all()
    return render(request, 'booking/packages_list.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    return render(request, 'booking/package_detail.html', {'package': package})


def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == "POST":
        form = PackageBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.total_price = package.price  # السعر الكامل من الباكدج
            booking.remaining_amount = package.price - booking.paid_amount  # حساب المتبقي
            booking.save()
            return redirect('booking_success')  # سيتم إنشاء صفحة نجاح لاحقًا
    else:
        form = PackageBookingForm()
    return render(request, 'booking/book_package.html', {'form': form, 'package': package})

def booking_success(request):
    return render(request, 'booking/booking_success.html')
