from django.urls import path
from . import views

app_name='address'

urlpatterns = [
    path('', views.shipping_address, name='shipping_addresses'),
    path('crear/', views.create, name='createAddress'),
    path('editarDireccion/<int:id>', views.address_to_update, name='updateAnAddress'),
    path('editar/', views.update, name='update'),
    path('eliminar/<int:id>', views.delete, name='delete'),
    path("default/<int:pk>", views.default, name="default")
]
