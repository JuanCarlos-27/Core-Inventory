from . models import Order

def get_or_created_order(cart, request):
    order = cart.order
    
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
        
    if order:
        request.session['order_id'] = order.order_id
        
    return order