from django.contrib import admin
from django.utils.html import format_html
from . models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','user','created_at','total','shipping_address','Estado','pdf')
    exclude = ('status',)
    
    
    def pdf(self,queryset):
        if queryset.status == 'OrderStatus.COMPLETED':
            print(queryset)
            return format_html('<a href="/pedidos/generatePDF/{}">📂<a/>', queryset)

    def Estado(self, obj):
        if obj.status == 'OrderStatus.COMPLETED':
            return format_html('<p class="bg-success rounded-pill font-weight-bold text-white p-1">Completado<p/>')
        elif obj.status == 'OrderStatus.CANCELED':
            return format_html('<p class="bg-primary text-center font-weight-bold rounded-pill text-white p-1">Cancelado<p/>')