from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
class Mail:
    def send_complete_order(order, user):
        subject = 'Tu pedido esta en camino 🚚'
        template = get_template('Pedidos/email_order_completed.html')
        content = template.render({
            'user':user
        })
        
        message = EmailMultiAlternatives(
            subject,
            'Mensaje importante',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        
        message.attach_alternative(content, 'text/html')
        message.send()