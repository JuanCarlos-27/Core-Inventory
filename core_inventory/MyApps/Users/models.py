from django.db import models
from django.contrib.auth.models import AbstractUser
from MyApps.Orders.common import OrderStatus

class User(AbstractUser):
    email = models.EmailField(('Correo electrónico'), unique=True)
    phone_number = models.CharField(max_length=10, unique=True, verbose_name="Teléfono")
    dni = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    address = models.CharField(max_length=60)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def shippingAddress(self):
        return self.shippingaddress_set.filter(default=True).first()
    
    def has_shipping_address(self):
        return self.shippingAddress is not None
    
    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')