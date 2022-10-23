from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import Product

class ProductResources(resources.ModelResource):
    fields = ('id_product','name','descripction','price','show_image','stock','status')
    class Meta:
        model = Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    fields = ('name','descripction','price','image_product','stock','status')
    list_display = ('id_product','name','descripction','price','show_image','stock','status',"slug")
    ordering = ("id_product",)
    search_fields = ('name', 'id_product')
    list_editable = ('status',)
    #list_filter = ()
    list_display_links = ("name",)

    