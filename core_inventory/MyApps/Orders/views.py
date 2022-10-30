from django.shortcuts import render
from MyApps.Carts.utils import create_cart
from . models import Order
from . utils import get_or_created_order, breadcrumb
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def order(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    return render(request, 'Pedidos/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb':breadcrumb()
    })