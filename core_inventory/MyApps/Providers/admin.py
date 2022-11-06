from django.contrib import admin
from . models import Supplier
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class SupplierResources(resources.ModelResource):
    fields = ('name','phone_number','web_page')
    class Meta:
        model = Supplier

@admin.register(Supplier)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('name','phone_number','web_page')