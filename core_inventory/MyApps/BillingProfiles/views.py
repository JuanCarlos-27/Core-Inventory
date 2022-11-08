from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from MyApps.Carts.utils import create_cart
from django.conf import settings
from . models import BillingProfile
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# class BillingProfileListView(LoginRequiredMixin, ListView):
#     login_url = 'login'
#     template_name='Pagos/billing_profiles.html'
    
#     def get_queryset(self):
#         return self.request.useSr.billing_profiles
    

@login_required(login_url='login')
def create(request):
    cart = create_cart(request)
    if request.method == 'POST':
        if request.POST.get('stripeToken'):
            if not request.user.has_customer():
                request.user.create_customer_id()
                #Puedo apartir del token filtrar y encontrar el card id del usuario.. IDEA
            stripe_token = request.POST['stripeToken']
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user,stripe_token)
            if billing_profile:
                messages.success(request, "¡Tarjeta creada correctamente!")
          
    billing_profiles=request.user.billing_profiles
    
    return render(request, 'Pagos/create.html',{
        "cart":cart,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "billing":billing_profiles
    })