# Generated by Django 4.1 on 2023-02-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(max_length=14, unique=True, verbose_name='Cédula'),
        ),
    ]