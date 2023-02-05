# Generated by Django 4.1 on 2022-11-07 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PromoCodes', '0002_alter_promocode_options_alter_promocode_code_and_more'),
        ('Orders', '0006_alter_order_options_alter_order_accepted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PromoCodes.promocode'),
        ),
    ]