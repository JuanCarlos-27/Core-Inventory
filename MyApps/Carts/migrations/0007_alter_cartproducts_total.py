# Generated by Django 4.1 on 2023-02-05 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0006_alter_cart_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproducts',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
