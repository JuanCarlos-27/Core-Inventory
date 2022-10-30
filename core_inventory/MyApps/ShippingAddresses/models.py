from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    reference = models.CharField(max_length=300)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
    def update_default(self, default=False):
        self.default = default
        self.save()
        
    