from django.urls import path
from . import views

app_name = 'Purchase'

urlpatterns = [
    path('generatePDF/<info>', views.purchasePdf, name='generatePDF'),
]
