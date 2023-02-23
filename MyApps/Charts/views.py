from django.shortcuts import render
from MyApps.Orders.models import Order
from MyApps.Orders.common import OrderStatus
from MyApps.Sales.models import Sale
from django.http import JsonResponse
from . utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

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
        order_filter=order.extra(where=[f"MONTH(created_at) = {month_number}"]).count()
        data.append(order_filter)
    
    print(data)
    return JsonResponse({
        'title': f'Pedidos por mes en el año {year}',
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


@login_required(login_url='login')
def earning_total_per_month(request,year):
    order = Order.objects.filter(created_at__year = year)
    sales = Sale.objects.filter(created_at__year=year)
    months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    data = []
    totales = []
    for month_number in range(1,13):
        orders_month = order.extra(where=[f"MONTH(created_at) = {month_number}"])
        sales_month = sales.extra(where=[f"MONTH(created_at) = {month_number}"])

        for order_total in orders_month:
            totales.append(order_total.total)
        for sale_total in sales_month:
            totales.append(sale_total.total)
            
        data.append(sum(totales))
        totales = []
    
    return JsonResponse({
        'title': f'Total ingresos por mes en {year}',
        'data': {
            'labels': months,
            'datasets': [{
                'label': year,
                'data': data,
                'lineTension': 0,
                'fill': False,
                'borderColor':"orange",
                'backgroundColor':"transparent", 
                'pointBorderColor': "orange",
                'pointBackgroundColor': 'rgba(255,150,0,0.5)',
                'pointRadius': 5,
                'pointHoverRadius': 10,
                'pointHitRadius': 30,
                'pointBorderWidth': 2,
                'pointStyle': 'rectRounded'
            }]
        },
    })