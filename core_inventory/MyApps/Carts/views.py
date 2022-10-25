from django.shortcuts import render
from . models import Cart
from . utils import create_cart #Aqui se creó el metodo
from MyApps.Products.models import Product
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from . models import CartProducts

def cart(request):
    cart = create_cart(request)
    # print(cart.products.count())
    return render(request, "Carrito/cart.html", {
        "cart": cart
        })
    
def add(request):
    cart = create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))
    quantity = int(request.POST.get('txtQuantity', 1)) # Por defecto 1    

    # cart.products.add(product, through_defaults={
    #     'quantity':quantity
    # })
    cart_product = CartProducts.objects.create_or_update_quantity(
        cart=cart, 
        product = product, 
        quantity = quantity
    )
    
    new_stock = product.stock - quantity
    product.stock = new_stock
    product.save()

    messages.success(request, "¡{0} productos agregados!".format(quantity))
    
    return render(request, 'Carrito/productDetail.html',{"product": product})

def remove(request):
    cart = create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))
    
    #Si se elimina del carrito, el stock se restablece
    p = cart.cartproducts_set.get(product_id = request.POST.get('product_id'))
    product.stock = product.stock + p.quantity
    product.save()

    cart.products.remove(product)
    messages.success(request, "¡Producto eliminado!")
    return redirect('Carts:cart')
    
