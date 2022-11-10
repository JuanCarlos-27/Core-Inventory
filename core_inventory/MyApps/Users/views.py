from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import User
from django.contrib import messages

@login_required(login_url='login')
def user_info(request):
    # new_name = request.POST['new_name']
    # new_last_name = request.POST['new_last_name']
    
    # user = User.objects.filter(email=request.user.email)
    
    # user.first_name = new_name
    # user.last_name = new_last_name
    # user.save()
    
    return render(request, 'Perfil/info_user.html')

def change(request):
    if request.method == 'POST':
        new_name = request.POST['new_name']
        user = User.objects.filter(email=request.user.email).first()
        
        user.first_name=new_name
        user.save()
        messages.success(request,"¡Has modificado tus datos!")

    return redirect('Users:user_info')