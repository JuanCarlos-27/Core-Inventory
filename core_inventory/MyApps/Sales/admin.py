from django.contrib import admin
from django.utils.html import format_html
from .models import Sale, SaleDetail
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SaleDetailInline(admin.TabularInline):
    model = SaleDetail
    extra = 1
    exclude = ['total',]
    
class SaleResources(resources.ModelResource):
    class Meta:
        model = Sale
    
class SaleAdmin(ImportExportModelAdmin):
    inlines = [SaleDetailInline,]
    filter_horizontal = ['product',]
    list_display = ('sale_id','created_at', 'total', 'pdf')
    exclude = ['sale_id','total', 'sale_man']
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def pdf(self,queryset):
        return format_html('<a class="text-decoration-none" href="/ventas/generatePDF/{}"><i class="fas fa-file text-primary"></i></a>', queryset)
    

admin.site.register(Sale, SaleAdmin)