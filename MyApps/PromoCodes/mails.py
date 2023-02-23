from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Mail:
    def send_promo_code(promo_code, user):
        subject = '🎁 Código de descuento 🎁'
        template = get_template('Promocion/email_promo_code.html')
        content = template.render({
            'promo_code':promo_code,
            'user':user,
        })
        
        message = EmailMultiAlternatives(
            subject,
            'Mensaje importante',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        
        message.attach_alternative(content, 'text/html')
        message.send()