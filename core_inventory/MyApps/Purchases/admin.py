from django.contrib import admin

from .models import Purchase, PurchaseDetail

class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail
    extra = 1
    exclude = ['total',]

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseDetailInline,]
    filter_horizontal = ['product',]
    list_display = ('purchase_id','created_at', 'total')
    exclude = ['purchase_id','total']
    



admin.site.register(Purchase, PurchaseAdmin)
