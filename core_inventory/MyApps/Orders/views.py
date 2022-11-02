from django.shortcuts import render, redirect, get_object_or_404
from MyApps.Carts.utils import create_cart, destroy_cart
from MyApps.Products.models import Product
from . models import Order
from . utils import get_or_created_order, breadcrumb, destroy_order
from django.contrib.auth.decorators import login_required
from MyApps.ShippingAddresses.models import ShippingAddress
from django.contrib import messages

@login_required(login_url='login')
def order(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    return render(request, 'Pedidos/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb':breadcrumb()
    })

@login_required(login_url='login')
def address(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1
    return render(request, 'Pedidos/address.html',{
        "cart":cart,
        "order": order,
        "shipping_address":shipping_address,
        'breadcrumb':breadcrumb(address=True),
        "can_choose_address":can_choose_address
    })
    
@login_required(login_url='login')
def select_address(request):
    shipping_addresses = request.user.shippingaddress_set.all()
    return render(request, 'Pedidos/select_address.html',{
        'breadcrumb':breadcrumb(address=True),
        'shipping_addresses':shipping_addresses
        
    })

@login_required(login_url='login')
def check_address(request, pk):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)
    
    if request.user.id != shipping_address.user_id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    order.update_shipping_address(shipping_address)
    messages.success(request, "¡Has cambiado tu direccion de envio!")
    return redirect('Orders:address')

@login_required(login_url='login')
def confirm(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    shipping_address = order.shipping_address
    
    if shipping_address is None:
        return redirect('Orders:address')
    
    return render(request, 'Pedidos/confirm.html',{
        'cart':cart,
        'order':order,
        'shipping_address': shipping_address,
        'breadcrumb':breadcrumb(address=True, confirmation=True),
    })
    

@login_required(login_url='login')
def cancel(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    if request.user.id != order.user_id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    if cart.cartproducts_set.all():
        for p in cart.cartproducts_set.all():
            product = get_object_or_404(Product, pk = p.product_id)
            product.stock = product.stock + p.quantity
            product.save()
            
    order.cancel()
    destroy_cart(request)
    destroy_order(request)
    messages.success(request, "¡Tu proceso de pedido ha sido cancelado!")

    return redirect('index')

@login_required(login_url='login')
def complete(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    if request.user.id != order.user_id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    order.complete()
    destroy_cart(request)
    destroy_order(request)
    
    return render(request, 'Pedidos/success_order.html',{
        
    })