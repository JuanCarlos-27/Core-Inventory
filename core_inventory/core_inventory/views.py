import threading
from datetime import timedelta
from django.shortcuts import render
from MyApps.Products.models import Product
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from MyApps.Carts.utils import create_cart, get_cantidad
from MyApps.PromoCodes.models import PromoCode
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic.list import ListView

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
    cart = create_cart(request)
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
                                            dni = dni)
        except Exception as e:
            messages.error(request, "Ya estas registrado")
            
        if user:
            thread = threading.Thread(target=send_success_registration, args=(
                email, name, password
            ))
            thread.start() 
            #Se crea un código de promoción para el usuario que se registra
            valid_from = user.date_joined
            valid_to = valid_from + timedelta(days=14)     
            PromoCode.objects.create(user=user,
                                     valid_from=valid_from,
                                     valid_to=valid_to,
                                     discount=1000)
            #Se 
            messages.success(request, "¡Te has registrado correctamente!")
            
            
            return redirect("login")
        
    return render(request, 'register.html', {"cart":cart})

def login_view(request):
    cart = create_cart(request)
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
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET['next'])
                return redirect("index")
            
            
        else:
            messages.error(request, "Usuario y/o contraseña no validos")
        
    return render(request, 'login.html', {"cart":cart})

def logout_view(request):
    cart = create_cart(request)
    if cart.cartproducts_set.all():
        for p in cart.cartproducts_set.all():
            product = get_object_or_404(Product, pk = p.product_id)
            product.stock = product.stock + p.quantity
            product.save()
        logout(request)
    else:
        logout(request)
    
    messages.success(request, "¡Sesión cerrada correctamente!")
    return redirect("login")

# def productosCatalogo(request):
#     cart = create_cart(request)
#     # print(cart.products.count())
#     listaProductos = Product.objects.all()
#     return render(request, "index.html", {
#         "productos":listaProductos,
#         "cart": cart
#         })

class ProductListView(ListView):
    def cart(self):
        cart = create_cart(self.request)
        return cart
    def promo_codes(self):
        if self.request.user.is_authenticated:
            promo_code = PromoCode.objects.has_promo_code(self.request.user)
            return promo_code

    
    template_name='index.html'
    queryset = Product.objects.all()
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart()
        context['promo_code'] = self.promo_codes()
        return context
    
def contact(request):
    cart = create_cart(request)
    if request.method == 'POST':
        name = request.POST['nameContact']
        email = request.POST['emailContact']
        subject = request.POST['subject']
        message = request.POST['messageContact']
        context = {
            'name': name,
            'email': email,
            'message': message,
            'subject':subject
        }
        template = get_template("contact_email.html")
        content = template.render(context)
        email = EmailMultiAlternatives(
            subject,
            "Mensaje de contacto",
            settings.EMAIL_HOST_USER,
            ['noemply.inventory@gmail.com']
        )
        email.attach_alternative(content, 'text/html')
        email.send()
        messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")

    return render(request, "contact.html",{"cart":cart})

def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')