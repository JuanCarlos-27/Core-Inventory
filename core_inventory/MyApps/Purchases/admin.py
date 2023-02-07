from django.contrib import admin
from django.utils.html import format_html
from .models import Purchase, PurchaseDetail

class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail
    extra = 1
    exclude = ['total',]
    
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseDetailInline,]
    filter_horizontal = ['product',]
    list_display = ('purchase_id','created_at', 'total', 'pdf')
    exclude = ['purchase_id','total']
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def pdf(self,queryset):
        return format_html('<a class="text-decoration-none" href="/compras/generatePDF/{}">📂<a/>', queryset)

admin.site.register(Purchase, PurchaseAdmin)
