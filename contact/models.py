from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    

class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)  # اسم الشركة
    logo = models.ImageField(upload_to='static/images/logo/', blank=True, null=True)  # اللوجو
    address = models.TextField()  # العنوان
    phone_number = models.CharField(max_length=20)  # رقم الهاتف
    facebook_link = models.URLField(blank=True, null=True)  # فيسبوك
    whatsapp_link = models.URLField(blank=True, null=True)  # واتساب
    instagram_link = models.URLField(blank=True, null=True)  # إنستجرام
    tiktok_link = models.URLField(blank=True, null=True)  # تيك توك

    def __str__(self):
        return self.name

