# Generated by Django 4.1 on 2023-02-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetail',
            name='quantity',
            field=models.IntegerField(verbose_name='cantidad'),
        ),
        migrations.AlterModelTable(
            name='purchase',
            table='purchase',
        ),
        migrations.AlterModelTable(
            name='purchasedetail',
            table='purchase_detail',
        ),
    ]
