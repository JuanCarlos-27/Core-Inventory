# Generated by Django 4.1 on 2023-02-04 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
