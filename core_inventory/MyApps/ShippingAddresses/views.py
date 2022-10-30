from django.shortcuts import render
from django.views.generic import ListView
from . models import ShippingAddress
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='login'), name='dispatch')
class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = "Direcciones/shipping_addresses.html"

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
    