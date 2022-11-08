from django.contrib import admin
from .models import PromoCode
# Register your models here.

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    exclude = ['code']