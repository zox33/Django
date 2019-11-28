from django.db import models

# Create your models here.


class Categoria(models.Model):
    
    nombre= models.CharField(("Nombre"), max_length=50)
    categoria_padre= models.ForeignKey('Categoria', related_name="Categorias",blank=True,on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre= models.CharField(("Nombre"), max_length=50)
    descripcion= models.TextField(("Descripcion"), max_length=4000)
    url_imagen= models.URLField(("Imagen"), max_length=2000, blank=True)
    precio_unidad= models.DecimalField(("Precio"), max_digits=5, decimal_places=2)
    categoria= models.ForeignKey('Categoria', related_name="Categoria", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre




