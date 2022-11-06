from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Cliente")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    neighborhood = models.CharField(max_length=100, verbose_name="Barrio")
    zone = models.CharField(max_length=100, verbose_name="Localidad")
    reference = models.CharField(max_length=300, verbose_name= "Referencias")
    default = models.BooleanField(default=False, verbose_name= "Dirección principal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Registrada el")
    
    def __str__(self):
        return self.address
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
    
    def has_orders(self):
        return self.order_set.count() >= 1
    
    def update_default(self, default=False):
        self.default = default
        self.save()
        
    