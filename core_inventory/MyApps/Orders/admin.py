from django.contrib import admin
from . models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','user','created_at','total','shipping_address','status','accepted')
    exclude = ('status',)
    list_editable = ('accepted',)