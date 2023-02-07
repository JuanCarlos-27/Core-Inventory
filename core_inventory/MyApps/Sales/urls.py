from django.urls import path
from . import views

app_name = 'Sale'

urlpatterns = [
    path('generatePDF/<info>', views.salesPdf, name='generatePDF'),
]
