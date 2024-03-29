import uuid
from django.db import models
from MyApps.Providers.models import Supplier
from MyApps.Products.models import Product
from django.db.models.signals import pre_save, m2m_changed, post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver

class Purchase(models.Model):
    purchase_id = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Id")
    product = models.ManyToManyField(Product, through="PurchaseDetail")
    total = models.IntegerField(default=0, verbose_name="Total pago")
    provider = models.ForeignKey(Supplier, verbose_name="Proovedor", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    
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
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE,
                                verbose_name="Producto", blank=False)
    quantity = models.IntegerField(
        default=0, verbose_name="cantidad", null=False, blank=False)
    unit_price = models.IntegerField(
        default=0, verbose_name="Precio unitario", null=False, blank=False)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.unit_price or self.unit_price < 50:
            raise ValidationError("El precio unitario debe ser mayor a $50")
        
        if not self.quantity or self.quantity == 0:
            raise ValidationError("Debe ingresar un valor valido para la cantidad")


    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Detalle compra"
        verbose_name_plural = "Detalle compras"
        db_table = "purchase_detail"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.quantity * instance.unit_price


pre_save.connect(set_total, sender=PurchaseDetail)


def set_total_purchase(sender, instance, *args, **kwargs):
    obj = instance.purchase
    obj.total += instance.total
    obj.save()


pre_save.connect(set_total_purchase, sender=PurchaseDetail)


def update_stock(sender, instance, *args, **kwargs):
    obj = instance.product
    obj.stock += instance.quantity
    obj.save()


pre_save.connect(update_stock, sender=PurchaseDetail)
