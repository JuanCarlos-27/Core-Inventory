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
    path("completado", views.complete, name="complete"),
    path("mensaje_exito", views.success, name="success"),
    path("mis_pedidos", views.OrderListView.as_view(), name="orders_list"),
    path("mis_pedidos/cancelados", views.orders_cancelled, name="orders_cancelled"),

]
