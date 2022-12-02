from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.ProductListView.as_view(), name='index'), # Ruta raiz
    path('main/', include('MyApps.Products.urls')),
    path('carrito/', include('MyApps.Carts.urls')),
    path('pedidos/', include('MyApps.Orders.urls')),
    path('product_detail/', include('MyApps.Products.urls')),
    path('pagos/', include('MyApps.BillingProfiles.urls')),
    path('codigos/', include('MyApps.PromoCodes.urls')),
    path('perfil/', include('MyApps.Users.urls')),
    path('login', views.login_view, name='login'), # Login
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('contacto', views.contact, name='contact'),
    path('direcciones/', include('MyApps.ShippingAddresses.urls')),
    path('graficos/', include('MyApps.Charts.urls')),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="Password/forgot_password.html"), name="password_reset"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="Password/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="Password/password_reset_complete.html"), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="Password/change_password.html"), name="change_password"),
    path('change-success/', auth_views.PasswordChangeDoneView.as_view(template_name="Password/password_change_done.html"), name="password_change_done"),

]
# 404 redirect
handler404 = views.error_404_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)