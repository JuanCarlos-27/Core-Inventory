# Generated by Django 4.1 on 2022-11-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PromoCodes', '0002_alter_promocode_options_alter_promocode_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='send',
            field=models.BooleanField(default=False, verbose_name='¿Ya fue enviado?'),
        ),
    ]
