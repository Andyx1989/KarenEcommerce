# Generated by Django 4.0.2 on 2022-02-15 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre del Producto')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=500, unique=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio')),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField(verbose_name='Existencias')),
                ('is_available', models.BooleanField(default=True, verbose_name='Disponible?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Categoria')),
            ],
        ),
    ]
