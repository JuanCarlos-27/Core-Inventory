from . models import Order
from django.urls import reverse
def get_or_created_order(cart, request):
    order = cart.order
    
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
        
    if order:
        request.session['order_id'] = order.order_id
        
    return order

def breadcrumb(products=True, address=False, payment=False,confirmation=False):
    return [
        {'title':'Productos', 'collapsed': products, 'url': reverse('Orders:order')},
        {'title':'Dirección', 'collapsed': address, 'url': reverse('Orders:order')},
        {'title':'Pago', 'collapsed': payment, 'url': reverse('Orders:order')},
        {'title':'Confirmación','collapsed': confirmation, 'url': reverse('Orders:order')}
    ]