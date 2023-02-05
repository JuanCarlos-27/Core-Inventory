import threading
from django.shortcuts import render, redirect
from django.http import JsonResponse
from . models import PromoCode
from MyApps.Carts.utils import create_cart
from MyApps.Orders.utils import get_or_created_order
from . mails import Mail
from django.contrib import messages


def validate(request):
    cart = create_cart(request)
    order = get_or_created_order(cart, request)
    
    code = request.GET.get('code')
    promo_code = PromoCode.objects.get_valid(code)
    
    if promo_code is None:
        return JsonResponse({
            'status':False,
        })

    order.apply_promo_code(promo_code)
    return JsonResponse({
        'status': True,
        'code': promo_code.code,
        'discount':promo_code.discount,
        'total':order.total
    })
    
def send_promo_code(request):
    promo_code=PromoCode.objects.filter(user=request.user).first()
    #Envio de correos de forma asincrona
    thread = threading.Thread(target=Mail.send_promo_code, args=(promo_code,request.user))
    thread.start()
    promo_code.send_to_user()
    messages.success(request, "¡Código enviado!")

    return redirect('index')