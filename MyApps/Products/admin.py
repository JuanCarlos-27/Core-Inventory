from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from .models import Product

class ProductResources(resources.ModelResource):
    fields = ('id_product','name','descripction','price','stock','status')
    class Meta:
        model = Product
        import_id_fields = ('id_product', )

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    form_template = 'product_form.html'
    resource_class = ProductResources
    fields = ('name','descripction','price','image_product','status')
    list_display = ('id_product','name','descripction','price','Imagen','stock','Estado')
    ordering = ("id_product",)
    search_fields = ('name', 'id_product')
    # list_editable = ('status',)
    #list_filter = ()
    list_display_links = ("name",)
    list_per_page = 10 # No. of records per page 
    
    def Imagen(self, obj):
        return format_html('<img src={} width="70" style="border-radius: 10px; filter:drop-shadow(0px 1px 2px #000); margin:0 10px;"/> ', obj.image_product.url)
    
    def Estado(self, obj):
        if obj.status == 1:
            return format_html("""
                               <div class="text-center">
                                   <p class="bg-primary text-center font-weight-bold rounded-pill text-white p-1">Agotado<p/>
                                   <a href="/admin/Purchases/purchase/add/#general-tab" target="_blank" class="text-center">Comprar</a>
                               </div>
                               """)
        return format_html('<p class="bg-success text-center rounded-pill font-weight-bold text-white p-1">Disponible<p/>')


