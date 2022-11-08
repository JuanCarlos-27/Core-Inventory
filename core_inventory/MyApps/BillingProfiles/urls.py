from django.urls import path
from . import views

app_name="billing"

urlpatterns = [
    path("nuevo", views.create, name="create"),
]
