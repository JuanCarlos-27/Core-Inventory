from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Sale, SaleDetail
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponse
from xhtml2pdf import pisa

@login_required(login_url='login')
def salesPdf(request, info):
    sale = Sale.objects.filter(sale_id = info).first()
    user = sale.client
    products = sale.saledetail_set.select_related('product')
    
    template = get_template("ReportesPDF/salesPdf.html")
    
    if not request.user.is_staff:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    context = {
        "sale": sale,
        "products": products,
        "user": user,
    }
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="venta ({sale.sale_id}).pdf"'
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response