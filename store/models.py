from django.urls import reverse
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre del Producto')
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, unique=True, verbose_name='Descripción')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Precio')
    images = models.ImageField(upload_to = 'photos/products')
    stock = models.IntegerField(verbose_name= 'Existencias')
    is_available = models.BooleanField(default=True, verbose_name= 'Disponible?')
    category = models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name= 'Categoria')
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de Modificación")

  
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created']

    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug])

    def __str__(self):
        return self.name