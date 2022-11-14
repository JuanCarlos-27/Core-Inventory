from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import User
from django.contrib import messages
from MyApps.Carts.utils import create_cart

@login_required(login_url='login')
def user_info(request):
    cart=create_cart(request)
    return render(request, 'Perfil/info_user.html',{'cart':cart})

def update_personal_information(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        new_last_name = request.POST.get('new_last_name')
        user = User.objects.filter(email=request.user.email).first()
        if new_name is None:
            new_name = user.first_name
        elif new_last_name is None:
            new_last_name = user.last_name
    
        user.first_name=new_name.strip()
        user.last_name=new_last_name.strip()
        user.save()
        messages.success(request,"¡Has modificado tus datos!")
    return redirect('Users:user_info')