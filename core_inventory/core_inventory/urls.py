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
    path('reset_password/', include('MyApps.Users.urls')),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="Password/password_reset_done.html"), name='password_reset_done'),
    path('login', views.login_view, name='login'), # Login
    path('logout', views.logout_view, name='logout'), # Register
    path('register', views.register, name='register'),
    path('contacto', views.contact, name='contact'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)