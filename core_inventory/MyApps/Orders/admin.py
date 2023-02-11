from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . models import Order

class OrderResources(resources.ModelResource):
    fields = ('order_id','user','created_at','total','shipping_address','status')
    class Meta:
        model = Order
        # import_id_fields = ('id_product', )

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_id','user','created_at','total','shipping_address','Estado',"Boton",'pdf')
    exclude = ('status',)
    
    
    def pdf(self,queryset):
        if queryset.status == 'OrderStatus.COMPLETED':
            return format_html('<a class="text-decoration-none" href="/pedidos/generatePDF/{}">📂<a/>', queryset)
        
        return format_html('<a class="text-decoration-none" href="/pedidos/generatePDF/{}"><i class="fas fa-file text-primary"></i><a/>', queryset)


    def Boton(self, queryset):
        if queryset.status != 'OrderStatus.CREATED':
            return format_html('<a href="#" class="btn btn-info disabled">Confirmado<a/>')
        else:
            return format_html("""
                               <div class="d-flex flex-wrap">
                                <a href="/pedidos/confirmar/{}" class="btn btn-info mb-1">Confirmar<a/>
                                <a href="/pedidos/cancelar_pedido/{}" class="btn btn-primary">Cancelar<a/>
                                </div>
                               """, queryset, queryset)


    def Estado(self, obj):
        if obj.status == 'OrderStatus.COMPLETED':
            return format_html('<p class="bg-success rounded-pill font-weight-bold text-white p-1">Completado<p/>')
        if obj.status == 'OrderStatus.CANCELED':
            return format_html('<p class="bg-primary text-center font-weight-bold rounded-pill text-white p-1">Cancelado<p/>')
        if obj.status == 'OrderStatus.CREATED':
            return format_html('<p class="bg-danger text-center font-weight-bold rounded-pill text-white p-1">En espera<p/>')