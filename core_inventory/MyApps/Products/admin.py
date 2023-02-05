from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Product



class ProductResources(resources.ModelResource):
    fields = ('id_product','name','descripction','price','stock','status')
    class Meta:
        model = Product
        import_id_fields = ('id_product', )

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResources
    fields = ('name','descripction','price','image_product','stock','status')
    list_display = ('id_product','name','descripction','price','show_image','stock','status')
    ordering = ("id_product",)
    search_fields = ('name', 'id_product')
    # list_editable = ('status',)
    #list_filter = ()
    list_display_links = ("name",)
    list_per_page = 10 # No. of records per page 
