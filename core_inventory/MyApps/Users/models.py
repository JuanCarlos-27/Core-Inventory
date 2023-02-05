from MyApps.stripeAPI.customer import create_customer
from django.db import models
from django.contrib.auth.models import AbstractUser
from MyApps.Orders.common import OrderStatus

class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=False)
    email = models.EmailField(('Correo electrónico'), unique=True)
    phone_number = models.CharField(max_length=10, unique=True, verbose_name="Teléfono")
    dni = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    # address = models.CharField(max_length=60)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "users"
        
    @property
    def shippingAddress(self):
        return self.shippingaddress_set.filter(default=True).first()
    @property
    def description(self):
        return 'Descripción para el usuario {}'.format(self.username)
    @property
    def billing_profiles(self):
        return self.billingprofile_set.all().order_by('-default')
    @property
    def billing_profile(self):
        return self.billingprofile_set.filter(default=True).first()    
    
    def has_shipping_address(self):
        return self.shippingAddress is not None
    
    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')
    
    def orders_unconfirmed(self):
        return self.order_set.filter(status=OrderStatus.CREATED).order_by('-id')
    
    def orders_cancelled(self):
        return self.order_set.filter(status=OrderStatus.CANCELED).order_by('-id')
    
    def has_customer(self):
        return self.customer_id is None
    
    def has_billing_profiles(self):
        return self.billingprofile_set.exists()
    
    def create_customer_id(self):
        if not self.has_customer():
            customer = create_customer(self)
            self.customer_id = customer.id
            self.save()