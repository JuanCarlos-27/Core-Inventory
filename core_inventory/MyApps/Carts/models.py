import uuid
import decimal
from django.db import models
from django.contrib.auth.models import User
from MyApps.Products.models import Product
from MyApps.Orders.common import OrderStatus
from django.db.models.signals import pre_save, m2m_changed, post_save
from django.contrib.auth import get_user_model
User = get_user_model()

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null = False, blank=False, unique = True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProducts')
    subtotal = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    FEE = 0 # Impuesto
    
    def __str__(self):
        return self.cart_id
    
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        db_table="carts"

        
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
        
        if self.order:
            self.order.update_total()
        
    def update_subtotal(self):
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
        ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()
        
    def products_related(self):
        return self.cartproducts_set.select_related('product')
    
    @property
    def order(self):
        return self.order_set.filter(status=OrderStatus.CREATED).first()

class CartProductsManager(models.Manager):
    def create_or_update_quantity(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)

        if not created:
            quantity = object.quantity + quantity
        
        total = quantity * product.price
        object.update_quantity(quantity)
        object.set_total(total)
        return object

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CartProductsManager()
    
    def update_quantity(self, quantity =1):
        self.quantity = quantity
        self.save()
        
    def set_total(self, total=0):
        self.total = total
        self.save()

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()
    
def change_product_status(sender, instance,*args, **kwargs):
    if instance.stock == 0:
        instance.status = 1
    else:
        instance.status = 0

pre_save.connect(set_cart_id, sender=Cart)
pre_save.connect(change_product_status, sender=Product)

post_save.connect(post_save_update_totals, sender = CartProducts)
m2m_changed.connect(update_totals, sender = Cart.products.through)
