from django.contrib import admin
from . models import BillingProfile

@admin.register(BillingProfile)
class BillingProfileAdmin(admin.ModelAdmin):
    pass