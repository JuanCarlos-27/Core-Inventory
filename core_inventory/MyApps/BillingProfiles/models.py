from django.db import models
from django.contrib.auth import get_user_model
from MyApps.stripeAPI.card import create_card
User = get_user_model()

# Create your models here.

class BillingProfileManager(models.Manager):
    def create_by_stripe_token(self, user, stripe_token):
        if not user.has_customer() and stripe_token:
            source =create_card(user, stripe_token)
            return self.create(card_id=source.id,
                               last4=source.last4,
                               token=stripe_token,
                               brand=source.brand,
                               user=user,
                               default= not user.has_billing_profiles())
            
    def delete_card_by_card_id(self, user, card_id):
        source=delete_card(user, card_id)
        return self.delete(card_id=source.id)

class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False, blank=False)
    card_id = models.CharField(max_length=50,null=False, blank=False)
    last4 = models.CharField(max_length=4, null=False, blank=False)
    brand = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = BillingProfileManager()
    
    def __str__(self):
        return self.card_id
    
    class Meta:
        verbose_name = "Método de pago"
        verbose_name_plural = "Métodos de pago"
        db_table="billing_profiles"

     