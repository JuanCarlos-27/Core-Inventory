from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.productosCatalogo, name='index'), # Ruta raiz
    path('main/', include('MyApps.Products.urls')),
    path('', include('MyApps.Customers.urls')),
    path('carrito/', include('MyApps.Carts.urls')),
    path('product_detail/', include('MyApps.Products.urls')),
    path('login', views.login_view, name='login'), # Login
    path('logout', views.logout_view, name='logout'), # Register
    path('register', views.register, name='register'), # Register
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)