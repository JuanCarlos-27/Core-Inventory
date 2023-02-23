# Generated by Django 4.1 on 2022-10-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0002_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]