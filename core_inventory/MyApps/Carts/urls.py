from django.urls import path
from . import views

app_name = "Carts"

urlpatterns = [
    path('', views.cart, name='cart'),
    path('agregar', views.add, name="add")
]
