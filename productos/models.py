from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Simple, sin decimales
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible?")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"