from django.db import models
from django import forms
from django.utils.html import format_html
# Create your models here.

PRODUCT_STATUS = (
    [0,'Disponible'],
    [1,'Agotado']
)
class Product(models.Model):
    id_product = models.AutoField(verbose_name="Código", primary_key=True, help_text = "Ej: 1")
    name = models.CharField(max_length=40, verbose_name= "Nombre" , help_text="Ej: Papaya")
    descripction = models.TextField(max_length=40, verbose_name="Descripcion",help_text="Ej: Und.x 100g")
    price = models.IntegerField(verbose_name="Precio",help_text="Ej: 12500")
    image_product = models.ImageField(upload_to = 'media', verbose_name="Imagen")
    stock = models.IntegerField(verbose_name="Cantidad", help_text="Ej: 50")
    status = models.IntegerField(verbose_name="Estado", choices= PRODUCT_STATUS, default="Disponible")
    

    def show_image(self):
        return format_html('<img src={} width="70" style="border-radius: 10px; border: 2px solid #000; margin:0 10px;"/> ', self.image_product.url)
    
    def show_image_catalog(self):
        return format_html('<img src={} alt="{}" width="200px" height="200px" class="img-responsive" /> ', self.image_product.url, self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "productos"