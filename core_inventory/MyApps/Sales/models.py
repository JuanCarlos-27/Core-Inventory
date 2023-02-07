import uuid
from django.db import models
from MyApps.Products.models import Product
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
User = get_user_model()

class Sale(models.Model):
    sale_id = models.CharField(max_length=100, null = False, blank = False, unique=True, verbose_name="Id")
    product = models.ManyToManyField(Product, through="SaleDetail")
    total = models.PositiveIntegerField(default=0, verbose_name="Total Ingreso")
    user = models.ForeignKey(User, verbose_name = "Cliente", on_delete = models.CASCADE)
    sale_man = models.IntegerField(default=0, verbose_name="Venta hecha por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha")
    
    def __str__(self):
        return self.sale_id
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        db_table = "sales"
        
    def set_sales_man(self, saleMan):
        self.sale_man = saleMan
        self.save()
    
def set_sale_id(sender, instance, *args, **kwargs):
    if not instance.sale_id:
        instance.sale_id = str(uuid.uuid4())[:7]
        # instance.set_sales_man(instance.)
     
pre_save.connect(set_sale_id, sender=Sale)

class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete = models.CASCADE)
    quantity = models.IntegerField(verbose_name="cantidad")
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Detalle de venta"
        verbose_name_plural = "Detalle de ventas"
        db_table = "sale_detail"
        
def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.quantity * instance.product.price
    
pre_save.connect(set_total, sender=SaleDetail)

def set_total_sale(sender, instance, *args, **kwargs):
    obj = instance.sale
    obj.total += instance.total
    obj.save()

post_save.connect(set_total_sale,sender=SaleDetail)

def update_stock(sender, instance, *args, **kwargs):
    obj = instance.product
    obj.stock -= instance.quantity
    obj.save()
        
post_save.connect(update_stock,sender=SaleDetail)