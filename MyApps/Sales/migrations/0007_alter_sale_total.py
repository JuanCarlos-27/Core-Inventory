# Generated by Django 4.1 on 2023-02-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0006_alter_saledetail_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.IntegerField(default=0, verbose_name='Total Ingreso'),
        ),
    ]
