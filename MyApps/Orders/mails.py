from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import date
class Mail:
    def send_complete_order(order, user, cart):
        today = date.today()
        subject = 'Tu pedido esta en camino 🚚'
        template = get_template('Pedidos/email_order.html')
        content = template.render({
            'date':today,
            'user':user,
            'order':order,
            'cart':cart
        })
        
        message = EmailMultiAlternatives(
            subject,
            'Mensaje importante',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        
        message.attach_alternative(content, 'text/html')
        message.send()