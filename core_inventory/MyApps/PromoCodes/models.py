import string
import random
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

User = get_user_model()

class PromoCodeManager(models.Manager):
    def get_valid(self, code):
        now = timezone.now()
        return self.filter(code=code).filter(used=False).filter(valid_from__lte=now).filter(valid_to__gte=now).first()

    def has_promo_code(self,user):
        if user:
            return self.filter(user=user).first()


class PromoCode(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE, verbose_name="Cliente")
    code = models.CharField(max_length=50, unique=True, verbose_name="Código")
    discount = models.IntegerField(default=0, verbose_name="Descuento")
    valid_from = models.DateTimeField(verbose_name="Válido desde")
    valid_to = models.DateTimeField(verbose_name="Válido hasta")
    used = models.BooleanField(default=False, verbose_name="¿Ya fue usado?")
    send = models.BooleanField(default=False, verbose_name="¿Ya fue enviado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Generado el")
    
    
    def __str__(self):
        return self.code
    
    objects = PromoCodeManager()
    
    class Meta:
        verbose_name = "Código de promoción"
        verbose_name_plural = "Códigos de promoción"
        db_table="promo_codes"
        
    def use(self):
        self.used = True
        self.save()
        
    def send_to_user(self):
        self.send = True
        self.save()

def set_code(sender, instance, *args, **kwargs):
    if instance.code:
        return
    
    chars= string.ascii_uppercase + string.digits
    instance.code = ''.join( random.choice(chars) for _ in range(10) )

pre_save.connect(set_code, sender=PromoCode)