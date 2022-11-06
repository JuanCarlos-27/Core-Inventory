from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('dni','first_name','last_name','email','phone_number','date_joined','is_staff')