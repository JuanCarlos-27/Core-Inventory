# Generated by Django 4.1 on 2022-11-06 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShippingAddresses', '0002_rename_line1_shippingaddress_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Dirección', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registrada el'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Dirección principal'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='neighborhood',
            field=models.CharField(max_length=100, verbose_name='Barrio'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='reference',
            field=models.CharField(max_length=300, verbose_name='Referencias'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zone',
            field=models.CharField(max_length=100, verbose_name='Localidad'),
        ),
    ]