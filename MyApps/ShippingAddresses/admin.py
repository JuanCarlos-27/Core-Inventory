from django.contrib import admin
from . models import ShippingAddress
# Register your models here.

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user','address','neighborhood','zone','reference','default','created_at')