from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Purchase, PurchaseDetail
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponse
from xhtml2pdf import pisa

@login_required(login_url='login')
def purchasePdf(request, info):
    purchase = Purchase.objects.filter(purchase_id = info).first()
    provider = purchase.provider
    products = purchase.purchasedetail_set.select_related('product')
    template = get_template("ReportesPDF/purchasePdf.html")
    
    if not request.user.is_staff:
        messages.error(request, "¡Estas tratando de ingresar a urls no permitidas, por seguridad hemos registrado tus datos y tu dirección IP!")
        return redirect('index')
    
    context = {
        "purchase": purchase,
        "products": products,
        "provider": provider,
    }
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="compra ({purchase.purchase_id}).pdf"'
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response