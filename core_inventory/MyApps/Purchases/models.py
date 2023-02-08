import uuid
from django.db import models
from MyApps.Providers.models import Supplier
from MyApps.Products.models import Product
from django.db.models.signals import pre_save, m2m_changed, post_save
from django.core.exceptions import ValidationError


class Purchase(models.Model):
    purchase_id = models.CharField(max_length=100, null = False, blank = False, unique=True, verbose_name="Id")
    product = models.ManyToManyField(Product, through="PurchaseDetail")
    total = models.IntegerField(default=0, verbose_name="Total pago")
    provider = models.ForeignKey(Supplier, verbose_name = "Proovedor", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha")
    
    def __str__(self):
        return self.purchase_id
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        db_table = "purchase"
    
def set_purchase_id(sender, instance, *args, **kwargs):
    if not instance.purchase_id:
        instance.purchase_id = str(uuid.uuid4())[:7]
     
pre_save.connect(set_purchase_id, sender=Purchase)



class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="cantidad")
    unit_price = models.PositiveIntegerField(verbose_name="Precio unitario")
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Detalle compra"
        verbose_name_plural = "Detalle compras"
        db_table = "purchase_detail"
        
    def clean(self):
        obj = self.product
        
        if not self.quantity:
            raise ValidationError("Debe ingresar un valor valido")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)  
    
        
def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.quantity * instance.unit_price
    
pre_save.connect(set_total, sender=PurchaseDetail)

def set_total_purchase(sender, instance, *args, **kwargs):
    obj = instance.purchase
    obj.total += instance.total
    obj.save()
        
post_save.connect(set_total_purchase,sender=PurchaseDetail)

def update_stock(sender, instance, *args, **kwargs):
    obj = instance.product
    obj.stock += instance.quantity
    obj.save()
        
post_save.connect(update_stock,sender=PurchaseDetail)