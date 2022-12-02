from django.shortcuts import render
from MyApps.Orders.models import Order
from MyApps.Orders.common import OrderStatus
from django.http import JsonResponse
from . utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def statistics_view(request):
    return render(request, 'statistics.html', {})

@login_required(login_url='login')
def orders_success_vs_cancelled_char(request, year):
    order = Order.objects.filter(created_at__year=year)
    return JsonResponse({
        'title': f'Pedidos completados VS cancelados en {year}',
        'data': {
            'labels': ['Completados', 'Cancelados'],
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': [colorSuccess, colorDanger],
                'borderColor': [colorSuccess, colorDanger],
                'data': [
                    order.filter(status=OrderStatus.COMPLETED).count(),
                    order.filter(status=OrderStatus.CANCELED).count(),
                ],
            }]
        },
    })

@login_required(login_url='login')
def orders_per_month_chart(request,year):
    order = Order.objects.filter(created_at__year = year)
    data = []
    months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

    for month_number in range(1,13):
        data.append(order.filter(created_at__month = month_number).count())
        
    return JsonResponse({
        'title': f'Pedidos x mes',
        'data': {
            'labels': months,
            'datasets': [{
                'label': 'Pedidos',
                'backgroundColor': 'rgba(54, 162, 235, 0.6)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1,
                'data': data,
            }]
        },
    })
