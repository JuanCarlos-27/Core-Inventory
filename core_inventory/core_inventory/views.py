from django.shortcuts import render
from MyApps.Products.models import Product
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from MyApps.Carts.utils import create_cart

from django.contrib.auth import get_user_model
User = get_user_model()

def send_success_registration(emailUser, name, clave):
    context = {
        'name':name, 
        'email':emailUser,
        'clave': clave[:4]
        }
    template = get_template("email.html")
    content = template.render(context)
    
    email = EmailMultiAlternatives(
        'Correo de confirmación',
        'Tu registro ha sido exitoso',
        settings.EMAIL_HOST_USER,
        [emailUser]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def register(request):
    if request.method == 'POST':
        email = request.POST.get("correo")
        name = request.POST.get("nombre")
        last_name = request.POST.get("apellido")
        dni = request.POST.get("documento")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        username = request.POST.get("correo")
        password = request.POST.get("password")
        
        user = False
        try:
            user = User.objects.create_user(username=dni,
                                            email=email,
                                            password=password,
                                            first_name=name,
                                            last_name=last_name,
                                            phone_number=telefono,
                                            address = direccion,
                                            dni = dni)
        except Exception as e:
            messages.error(request, "Ya estas registrado")
            
        if user:
            send_success_registration(email, name, password)
            messages.success(request, "¡Te has registrado correctamente!")
            return redirect("login")
        
    return render(request, 'register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Si existe me retorna un objeto, de lo contrario retorna None.
        user = authenticate(email= email, password=password)
               
        if user:
            data_user = User.objects.get(email=user)
            full_name = data_user.first_name + " " + data_user.last_name 
            login(request, user)
            messages.success(request, "¡Bienvenido {}!".format(full_name))
            if data_user.is_staff:
                return redirect("admin/")
            else:
                return redirect("index")
        else:
            messages.error(request, "Usuario y/o contraseña no validos")
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "¡Sesión cerrada correctamente!")
    return redirect("login")

def productosCatalogo(request):
    cart = create_cart(request)
    # print(cart.products.count())
    listaProductos = Product.objects.all()
    return render(request, "index.html", {
        "productos":listaProductos,
        "cart": cart
        })
