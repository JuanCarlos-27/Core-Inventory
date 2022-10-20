from django.shortcuts import render
from MyApps.Products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("email")
        password = request.POST.get("password")
        # Si existe me retorna un objeto, de lo contrario retorna None.
        user = authenticate(username= username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "¡Bienvenido {}!".format(username))
            return redirect("index")
        else:
            messages.error(request, "Usuario y/o constraseña no validos")
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "¡Sesión cerrada correctamente!")
    return redirect("login")

def register(request):
    return render(request, 'register.html')

def productosCatalogo(request):
    user = request.user if request.user.is_authenticated else None

    if user != None:
        is_authenticated = True
    else:
        is_authenticated = False
        
    print(is_authenticated)
    listaProductos = Product.objects.all()
    return render(request, "index.html", {
        "productos":listaProductos,
        "is_authenticated":is_authenticated
        })
