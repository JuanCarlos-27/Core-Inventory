from django.contrib import admin
from django.utils.html import format_html
from .models import Purchase, PurchaseDetail
from django.http import FileResponse, HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django import forms
from django.forms import formset_factory
from django.core.exceptions import ValidationError


class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail
    extra = 1
    exclude = ['total',]

    
class PurchaseResources(resources.ModelResource):
    class Meta:
        model = Purchase


class PurchaseAdmin(ImportExportModelAdmin):
    inlines = [PurchaseDetailInline]
    filter_horizontal = ['product',]
    list_display = ('purchase_id','created_at', 'total', 'pdf')
    exclude = ['purchase_id','total']
    
    def has_change_permission(self, request, obj=None):
        return 
    
    def pdf(self,queryset):
        return format_html('<a class="text-decoration-none" href="/compras/generatePDF/{}"><i class="fas fa-file text-primary"></i><a/>', queryset)
        

admin.site.register(Purchase, PurchaseAdmin)
