# Generated by Django 4.1 on 2023-02-04 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PromoCodes', '0003_promocode_send'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='promocode',
            table='promo_codes',
        ),
    ]