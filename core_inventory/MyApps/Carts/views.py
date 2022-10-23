from django.shortcuts import render
from . models import Cart
from . utils import create_cart #Aqui se creó el metodo
from MyApps.Products.models import Product
from django.contrib import messages

def cart(request):
    user = request.user if request.user.is_authenticated else None
    if user != None:
        is_authenticated = True
    else:
        is_authenticated = False
        
    cart = create_cart(request)
    
    print(cart.products.all)
    return render(request, "Carrito/cart.html", {
        "is_authenticated":is_authenticated,
        "cart": cart
        })

def add(request):
    user = request.user if request.user.is_authenticated else None
    if user != None:
        is_authenticated = True
    else:
        is_authenticated = False
        
    cart = create_cart(request)
    product = Product.objects.get(pk = request.POST.get('product_id'))
    cart.products.add(product)
    messages.success(request, "¡Producto agregado!")
    context = {
        "product": product,
        "is_authenticated":is_authenticated
    }
    
    return render(request, 'Carrito/productDetail.html',context)
    
