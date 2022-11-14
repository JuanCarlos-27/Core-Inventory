import threading
import os
from django.shortcuts import render, redirect, get_object_or_404
from MyApps.Carts.utils import create_cart, destroy_cart
from MyApps.Products.models import Product
from MyApps.ShippingAddresses.models import ShippingAddress
from . models import Order
from . utils import get_or_created_order, breadcrumb, destroy_order
from . mails import Mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

@login_required(login_url='login')
def orderPdf(request, info):
    order = Order.objects.filter(order_id = info).first()
    template = get_template("ReportesPDF/orderPdf.html")
    
    if request.user.id != order.user.id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    context = {
        "products": order.cart.products.all(),
        "order": order,
    }
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="orden.pdf"'
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    
    return response




class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'Pedidos/orders_history.html'
    
    def cart(self):
        cart = create_cart(self.request)
        return cart
    
    def orders_canceller(self):
        return self.request.user.orders_cancelled()
    
    def get_queryset(self):
        return self.request.user.orders_completed()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart()
        context['orders_cancelled'] = self.orders_canceller()
        return context

@login_required(login_url='login')
def orders_cancelled(request):
    cart = create_cart(request)    
    orders_completed = request.user.orders_completed()
    orders_cancelled = request.user.orders_cancelled()
    return render(request, 'Pedidos/orders_cancelled.html', {
        'cart': cart,
        'order': order,
        'orders_cancelled':orders_cancelled,
    })

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
    
    print(can_choose_address)
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
        'breadcrumb':breadcrumb(address=True, confirmation=True, payment=True),
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
    messages.error(request, "¡Tu pedido ha sido cancelado!")

    return redirect('index')

@login_required(login_url='login')
def complete(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    if not order.shipping_address:
        destroy_order(request)
    
    if request.user.id != order.user_id:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')

    order.complete()
    #Envio de correos de forma asincrona
    thread = threading.Thread(target=Mail.send_complete_order, args=(
        order, request.user,cart
    ))
    thread.start()
    destroy_cart(request)
    destroy_order(request)
    messages.success(request, "¡Pedido exitoso!")
        
    return redirect('Orders:success')

@login_required(login_url='login')
def success(request):
    return render(request, 'Pedidos/success_order.html')

@login_required(login_url='login')
def payment(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    billing_profile = order.get_or_set_billing_profile()
    return render(request, 'Pedidos/payment.html',{
        "cart": cart,
        "order":order,
        "billing_profile":billing_profile,
        "breadcrumb": breadcrumb(address=True,payment=True)
    })
    