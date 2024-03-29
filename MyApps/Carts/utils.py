from . models import Cart

def create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get("cart_id")
    cart = Cart.objects.filter(cart_id = cart_id).first()
    
    if cart is None:
        cart = Cart.objects.create(user = user)
    
    if user and cart.user is None:
        cart.user = user
        cart.save()
        
    request.session['cart_id'] = cart.cart_id
    
    return cart

def get_cantidad(request):
    cart = create_cart(request)
    return cart.products.count()

def destroy_cart(request):
    request.session['cart_id']=None