from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=40, verbose_name = "Nombre", help_text="Ej: FruitLand")
    phone_number = models.CharField(max_length=40, verbose_name = "Télefono", help_text = "Ej: 3455668")
    web_page = models.CharField(max_length = 40, verbose_name = "Página web", help_text = "Ej: www.fruit.com")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "proveedor"