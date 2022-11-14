from django.db import models
from MyApps.Providers.models import Supplier
from MyApps.Products.models import Product

class Purchase(models.Model):
    provider = models.ForeignKey(Supplier, verbose_name = "Proovedor", on_delete = models.CASCADE)
    product = models.ManyToManyField(Product, through="DetalleCompra")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return created_at
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
            
class PurchaseDetail(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete = models.CASCADE)
    purchase = models.ForeignKey(Purchase, null=True,  on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="cantidad")
    
    def __str__(self):
        return str(self.product)
    
    class Meta:
        verbose_name = "Detalle compra"
        verbose_name_plural = "Detalle compras"