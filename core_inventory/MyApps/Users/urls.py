from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'Users'

urlpatterns = [
    path("informacion/", views.user_info, name="user_info"),
    path("actualizar-informaciom/", views.update_personal_information, name="update_personal_information"),
]
