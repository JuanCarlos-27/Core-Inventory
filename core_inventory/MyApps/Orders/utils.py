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
        {'title':'Productos', 'collapsed': products, 'progress':0, 'url': reverse('Orders:order')},
        {'title':'Dirección', 'collapsed': address,'progress':38,'url': reverse('Orders:address')},
        {'title':'Pago', 'collapsed': payment,'progress':68, 'url': reverse('Orders:payment')},
        {'title':'Confirmación','collapsed': confirmation,'progress':100,'url': reverse('Orders:order')}
    ]
    
def destroy_order(request):
    request.session['order_id'] = None