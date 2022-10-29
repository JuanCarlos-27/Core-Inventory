from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'Users'

urlpatterns = [
    path('', auth_views.PasswordResetView.as_view(template_name="Password/forgot_password.html"), name="password_reset"),
]
