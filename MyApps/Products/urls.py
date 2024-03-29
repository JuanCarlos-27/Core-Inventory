from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('productos_table/', views.vistaProducto),
    path('productos/registrarProducto', views.registrarProducto),
    path('productos/editarProducto', views.editarProducto),
    path('productos/productoAEditar/<id>', views.productoAEditar),
    path('productos/eliminarProducto/<id>', views.eliminarProducto),
    path('search', views.ProductSearchListView.as_view(), name="search"),
    path('<slug:slug>', views.productDetailView, name="product_detail")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)