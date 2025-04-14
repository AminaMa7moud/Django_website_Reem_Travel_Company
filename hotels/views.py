from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Review
from .forms import ReviewForm

def hotel_list(request):
    hotels = Hotel.objects.all()  # جلب كل الفنادق
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    reviews = hotel.review_set.all()  # جلب التقييمات المرتبطة بالفندق

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hotel = hotel
            review.save()
            return redirect('hotel_detail', hotel_id=hotel.id)  # إعادة تحميل الصفحة بعد الإضافة
    else:
        form = ReviewForm()

    return render(request, 'hotels/hotel_detail.html', {
        'hotel': hotel,
        'reviews': reviews,
        'form': form
    })
