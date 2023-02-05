# Generated by Django 4.1 on 2023-02-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0009_alter_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='accepted',
        ),
        migrations.AddField(
            model_name='order',
            name='cancelled_by',
            field=models.IntegerField(default=0, verbose_name='Tomar orden'),
        ),
    ]
