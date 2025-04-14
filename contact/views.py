from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import CompanyInfo
from contact.models import *


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إرسال رسالتك بنجاح! سنتواصل معك قريبًا.")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})




def contact_view(request):
    company = CompanyInfo.objects.first()  # جلب بيانات الشركة
    form = ContactForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "تم إرسال رسالتك بنجاح!")
    
    return render(request, "contact/contact.html", {"form": form, "company": company})
