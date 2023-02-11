import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from MyApps.Carts.models import Cart
from MyApps.PromoCodes.models import PromoCode
from MyApps.ShippingAddresses.models import ShippingAddress
from MyApps.BillingProfiles.models import BillingProfile
from . common import OrderStatus, choices
from django.utils.html import format_html
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
    promo_code = models.OneToOneField(PromoCode, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Código de promoción")
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True,on_delete=models.CASCADE, verbose_name="Info de pago")
    cancelled_by = models.IntegerField(default=0, verbose_name="Cancelado por")
    
    def __str__(self):
        return self.order_id
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "pedidos"
        db_table="orders"

    
    def apply_promo_code(self, promo_code):
        if self.promo_code is None:
            self.promo_code = promo_code
            self.save()
            self.update_total()
            promo_code.use()
        
    def get_or_set_billing_profile(self):
        if self.billing_profile:
            return self.billing_profile 
        billing_profile = self.user.billing_profile
        
        if billing_profile:
            self.update_billing_profile(billing_profile)

        return billing_profile    
    
    def update_billing_profile(self, billing_profile):
        self.billing_profile = billing_profile
        self.save()
        
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
    
    def created(self):
        self.status = OrderStatus.CREATED
        self.save()
        
    def cancel(self, user):
        self.status = OrderStatus.CANCELED
        self.cancelled_by = user.dni 
        self.save()
        
    def complete(self):
        self.status = OrderStatus.COMPLETED
        self.save()
        
    def cancelled(self):
        self.status = OrderStatus.CANCELED
        self.save()
    
    def update_total(self):
        self.total = self.get_total()
        self.save()
    
    def get_discount(self):
        if self.promo_code:
            return self.promo_code.discount       
        return 0
    
    def get_total(self):
        return self.cart.total + self.shipping_total - self.get_discount()

        
def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())[:5]

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()


pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)