from enum import Enum
import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from MyApps.Carts.models import Cart
from MyApps.ShippingAddresses.models import ShippingAddress

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
    shipping_address = models.ForeignKey(ShippingAddress, null=True, blank=True, on_delete=models.CASCADE)
    # employeed_in_charge = models.ManyToManyField(User)
    # accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.order_id
    
    def get_or_set_shipping_address(self):
        if self.shipping_address:
            return self.shipping_address
        
        shipping_address = self.user.shippingAddress
        if shipping_address:
            self.update_shipping_address(shipping_address)
            
        return shipping_address
    
    def update_shipping_address(self, shipping_address):
        self.shipping_address = shipping_address
        self.save()
    
    def cancel(self):
        self.status = OrderStatus.CANCELED
        self.save()
        
    def complete(self):
        self.status = OrderStatus.COMPLETED
        self.save()
    
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