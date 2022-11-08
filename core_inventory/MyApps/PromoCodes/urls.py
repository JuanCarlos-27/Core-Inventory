from django.urls import path
from . import views

app_name="promo_code"

urlpatterns = [
    path("validar",views.validate, name="validate"),
    path("enviar_code",views.send_promo_code, name="send_promo_code"),
    
]
