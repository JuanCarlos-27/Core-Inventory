# Generated by Django 4.1 on 2023-02-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_alter_saledetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saledetail',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='cantidad'),
        ),
    ]
