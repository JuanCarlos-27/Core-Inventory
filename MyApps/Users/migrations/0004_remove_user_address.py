# Generated by Django 4.1 on 2022-11-09 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_user_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
