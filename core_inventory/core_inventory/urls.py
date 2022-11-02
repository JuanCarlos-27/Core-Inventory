from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.productosCatalogo, name='index'), # Ruta raiz
    path('main/', include('MyApps.Products.urls')),
    path('carrito/', include('MyApps.Carts.urls')),
    path('pedidos/', include('MyApps.Orders.urls')),
    path('product_detail/', include('MyApps.Products.urls')),
    path('login', views.login_view, name='login'), # Login
    path('logout', views.logout_view, name='logout'), # Register
    path('register', views.register, name='register'),
    path('contacto', views.contact, name='contact'),
    path('direcciones/', include('MyApps.ShippingAddresses.urls')),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="Password/forgot_password.html"), name="password_reset"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="Password/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="Password/password_reset_complete.html"), name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)