from django.db import models
from django import forms
from django.utils.html import format_html
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid


PRODUCT_STATUS = (
    [0,'Disponible'],
    [1,'Agotado']
)
class Product(models.Model):
    id_product = models.AutoField(verbose_name="Código", primary_key=True, help_text = "Ej: 1")
    name = models.CharField(max_length=40, verbose_name= "Nombre" , help_text="Ej: Papaya")
    descripction = models.TextField(max_length=40, verbose_name="Descripcion",help_text="Ej: Und.x 100g")
    price = models.PositiveIntegerField(verbose_name="Precio",help_text="Ej: 12500")
    image_product = models.ImageField(upload_to = 'media', verbose_name="Imagen")
    stock = models.IntegerField(verbose_name="Cantidad", help_text="Ej: 50")
    status = models.IntegerField(verbose_name="Estado", choices= PRODUCT_STATUS, default="Disponible")
    slug = models.SlugField(null=False, blank=False, unique=True)

    def show_image(self):
        return format_html('<img src={} width="70" style="border-radius: 10px; border: 2px solid #000; margin:0 10px;"/> ', self.image_product.url)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "products"
        
def set_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        slug = slugify(instance.name)
        
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:4] )
            )
        instance.slug = slug
        
    
pre_save.connect(set_slug, sender=Product)