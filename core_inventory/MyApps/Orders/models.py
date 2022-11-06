import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from MyApps.Carts.models import Cart
from MyApps.ShippingAddresses.models import ShippingAddress
from . common import OrderStatus, choices

User = get_user_model()

class Order(models.Model):
    order_id = models.CharField(max_length=100, null = False, blank = False, unique=True, verbose_name="Id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length = 50, 
                              choices=choices, 
                              default=OrderStatus.CREATED, verbose_name="Estado")
    shipping_total = models.PositiveIntegerField(default=2000, verbose_name="Envio")
    total = models.PositiveIntegerField(default=0, verbose_name="Total pago")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    shipping_address = models.ForeignKey(ShippingAddress, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Dirección de envio")
    accepted = models.BooleanField(default=False, verbose_name="Tomar orden")
    # employeed_in_charge = models.ManyToManyField(User)
    def __str__(self):
        return self.order_id
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "pedidos"
        
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