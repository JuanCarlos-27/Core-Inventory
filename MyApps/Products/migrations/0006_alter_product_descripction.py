# Generated by Django 4.1 on 2023-02-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descripction',
            field=models.TextField(help_text='Ej: Und.x 100g', max_length=40, verbose_name='Descripción'),
        ),
    ]
