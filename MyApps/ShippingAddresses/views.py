from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView
from . models import ShippingAddress
from MyApps.Carts.utils import create_cart
from MyApps.Orders.utils import get_or_created_order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

# class ShippingAddressListView(LoginRequiredMixin,ListView):
#     login_url = 'login'  
#     model = ShippingAddress
#     template_name = "Direcciones/shipping_addresses.html"

#     def get_queryset(self):
#         return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
#     def notification(self):
#         cart = create_cart(self.request)
#         return cart
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart'] = self.notification()
#         return context

@login_required(login_url='login')
def shipping_address(request):
    cart = create_cart(request)
    shipping_addresses =  ShippingAddress.objects.filter(user=request.user).order_by('-default')


    return render(request, "Direcciones/shipping_addresses.html",{
        "cart":cart,
        "object_list":shipping_addresses
    })
    
@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        address = request.POST['address']
        neighborhood = request.POST['neighborhood']
        zone = request.POST['zone']
        reference = request.POST['reference']
        user = request.user
        
        shippingAddress_count = ShippingAddress.objects.filter(user=user).count()
        shippingAddress_default = ShippingAddress.objects.filter(user=user).exists()

        
        if shippingAddress_count < 3:
            if shippingAddress_default:
                shippingAddress = ShippingAddress.objects.create(user=user,address=address, neighborhood=neighborhood, zone=zone,reference=reference)
            else:
                shippingAddress = ShippingAddress.objects.create(user=user,address=address, neighborhood=neighborhood, zone=zone,reference=reference,default=True)
                
            messages.success(request, "¡Dirección creada correctamente!")
                            
        else:
            messages.error(request, "¡Ya has registrado suficientes direcciones!")
            
    return redirect('/direcciones')

@login_required(login_url='login')
def address_to_update(request, id):
    shippingAddress = ShippingAddress.objects.get(pk=id)
    
    if request.user.id != shippingAddress.user.id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')

    return render(request, "Direcciones/edit.html", {"shipping_address":shippingAddress})

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        shippingAddress = get_object_or_404(ShippingAddress, pk=request.POST['id'])
        shippingAddress.address = request.POST['address']
        shippingAddress.neighborhood = request.POST['neighborhood']
        shippingAddress.zone = request.POST['zone']
        shippingAddress.reference = request.POST['reference']
        shippingAddress.save()
        messages.success(request, "¡Dirección actualizada correctamente!")    
    return redirect('/direcciones')

@login_required(login_url='login')
def delete(request, id):
    shippingAddress = get_object_or_404(ShippingAddress, pk=id)
    
    if request.user.id != shippingAddress.user.id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    else:
        shippingAddress.delete()
    
    
    return redirect('/direcciones')

@login_required(login_url='login')
def default(request, pk):
    shippingAddress = get_object_or_404(ShippingAddress, pk=pk)
    
    if request.user.id != shippingAddress.user_id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')

    if request.user.has_shipping_address():
        request.user.shippingAddress.update_default()
    
    shippingAddress.update_default(True)
    messages.success(request, "¡Tu dirección principal ha cambiado!")
    
    return redirect('/direcciones')