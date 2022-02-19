from django.urls import reverse
from distutils.command.upload import upload
from operator import mod
from tabnanny import verbose
from turtle import update
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name= "Nombre de Categoría")
    description = models.CharField(max_length=255, blank= True, null= True, verbose_name= "Descripción")
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to = "photos/categories", blank = True, null = True, verbose_name= "Imagén")
    status = models.BooleanField(default= True, verbose_name= "Activo")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de Modificación")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name
