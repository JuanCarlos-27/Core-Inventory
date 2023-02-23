from django.urls import path
from . import views

app_name = 'Orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('direccion', views.address, name='address'),
    path('seleccionar/direccion', views.select_address, name='select_address'),
    path("establecer/direccion/<int:pk>", views.check_address, name="check_address"),
    path("confirmacion", views.confirm, name="confirm"),
    path("cancelar", views.cancel, name="cancel"),
    path("cancelar_pedido/<orderId>", views.cancel_order_created, name="cancel_order_created"),
    path("creado", views.created, name="created"),
    path("confirmar/<orderId>", views.complete, name="completed"),
    path("mensaje_exito", views.success, name="success"),
    path("mis_pedidos", views.OrderListView.as_view(), name="orders_list"),
    path("mis_pedidos/cancelados", views.orders_cancelled, name="orders_cancelled"),
    path("mis_pedidos/en_proceso", views.orders_unconfirmed, name="orders_unconfirmed"),
    path("pago", views.payment, name="payment"),
    path('generatePDF/<info>', views.orderPdf, name='generatePDF'),
]
