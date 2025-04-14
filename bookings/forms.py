from django import forms
from .models import PackageBooking

class PackageBookingForm(forms.ModelForm):
    class Meta:
        model = PackageBooking
        fields = ['full_name', 'phone_number', 'travel_date', 'return_date', 'pickup_location', 'paid_amount']

        labels = {
            'full_name': "الاسم الكامل",
            'phone_number': "رقم الهاتف",
            'travel_date': "تاريخ التحرك",
            'return_date': "تاريخ العودة",
            'pickup_location': "مكان التحرك",
            'paid_amount': "المبلغ المدفوع",
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسمك الكامل'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم هاتفك'}),
            'travel_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مكان التحرك'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'المبلغ المدفوع'}),
        }
