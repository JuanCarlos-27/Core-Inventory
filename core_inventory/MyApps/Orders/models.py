from enum import Enum
import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from MyApps.Carts.models import Cart

User = get_user_model()

class OrderStatus(Enum):
    CREATED = 'EN PROCESO'
    PAYED = 'PAGADO'
    COMPLETED = 'FINALIZADO'
    CANCELED = 'CANCELADO'
    
choices = [(tag, tag.value) for tag in OrderStatus]

class Order(models.Model):
    order_id = models.CharField(max_length=100, null = False, blank = False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length = 50, 
                              choices=choices, 
                              default=OrderStatus.CREATED)
    shipping_total = models.PositiveIntegerField(default=2000)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order_id
    
    def update_total(self):
        self.total = self.get_total()
        self.save()
    
    def get_total(self):
        return self.cart.total + self.shipping_total
    
def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())[:5]

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()


pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)