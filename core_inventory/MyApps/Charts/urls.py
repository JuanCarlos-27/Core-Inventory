from django.urls import path

from . import views

app_name='charts'

urlpatterns = [
    path('statistics/', views.statistics_view, name='shop-statistics'),  # new
    path('chart/order-success/<int:year>/', views.orders_success_vs_cancelled_char, name='chart-order-success'),
    path('chart/orders-per-month/<int:year>/', views.orders_per_month_chart, name='orders-per-month'),
    path('chart/earning-total-per-month/<int:year>/', views.earning_total_per_month, name='earning_total_per_month'),
]