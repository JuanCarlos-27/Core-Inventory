from django.urls import path
from . import views

app_name='address'

urlpatterns = [
    path('', views.ShippingAddressListView.as_view(), name='shipping_addresses')
]
