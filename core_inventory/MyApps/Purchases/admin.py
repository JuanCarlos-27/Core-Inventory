from django.contrib import admin

from .models import Purchase, PurchaseDetail

admin.site.register(Purchase)
admin.site.register(PurchaseDetail)