# Generated by Django 3.2.8 on 2022-02-18 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]