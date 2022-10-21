from django.shortcuts import render
from . models import Cart
from . utils import create_cart
from MyApps.Products.models import Product

# Create your views here.
def cart(request):
    user = request.user if request.user.is_authenticated else None
    if user != None:
        is_authenticated = True
    else:
        is_authenticated = False
        
    cart = create_cart(request)
    return render(request, "Carrito/cart.html", {"is_authenticated":is_authenticated})

def add(request):
    cart = create_cart(request)
    product = Product.objects.get(pk = request.POST.get('product_id'))
    cart.products.add(product)
    
    context = {
        "product": product
    }
    
    return render(request, 'Carrito/add.html',context)
    