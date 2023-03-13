import threading
from django.contrib import admin
from MyApps.PromoCodes.models import PromoCode
from datetime import datetime,timedelta
from django.utils import timezone
from django.contrib import messages
from .models import User
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_promo_code_email(promo_code, userEmail,user):
    subject = '🎁 Código de descuento 🎁'
    template = get_template('Promocion/email_promo_code.html')
    content = template.render({
        'promo_code':promo_code,
        'user':user
    })
    message = EmailMultiAlternatives(
        subject,
        'Mensaje importante',
        settings.EMAIL_HOST_USER,
        [userEmail]
    )
    message.attach_alternative(content, 'text/html')
    message.send()

def send_promo_code(modeladmin, request, queryset):
    #Definimos las fechas de expiración para cada código
    valid_from = timezone.now()
    valid_to = valid_from + timedelta(days=14)
    
    try:
        """ 
        El método range() recibe la cantidad de filas seleccionadas por
        el usuario e itera esa misma cantidad de veces.
        Luego, se crea un nuevo código por cada iteración y se le asigna
        al cliente correspondiente para posteriormente ejecutar el método
        de eviar el correo, el cual se ejecuta de forma asincrona.
        """
        for index in range(queryset.count()):
            user = User.objects.get(id=queryset[index].id)
            promoCode = PromoCode.objects.create(user_id=user.id,
                                    valid_from=valid_from,
                                    valid_to=valid_to,
                                    discount=1000)


            thread = threading.Thread(target=send_promo_code_email, args=(
                promoCode, queryset[index].email, user
            ))
            thread.start()
            promoCode.send_to_user()
        messages.success(request, "¡Codigos enviados correctamente!")
    except:
        messages.err(request, "¡Codigos enviados correctamente!")

send_promo_code.short_description = 'Enviar código de descuento'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('dni','first_name','last_name','email','phone_number','date_joined','is_staff')
    exclude = ('customer_id',)

    actions = [send_promo_code]