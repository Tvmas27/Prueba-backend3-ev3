# productos/admin.py
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista
    list_display = ['id', 'nombre', 'precio', 'stock', 'disponible', 'fecha_creacion']
    
    # Campos por los que se puede filtrar
    list_filter = ['disponible', 'fecha_creacion']
    
    # Campos por los que se puede buscar
    search_fields = ['nombre', 'descripcion']
    
    # Campos que se pueden editar directamente en la lista
    list_editable = ['precio', 'stock', 'disponible']
    
    # Campos de solo lectura
    readonly_fields = ['fecha_creacion']
    
    # Campos para ordenar
    ordering = ['-fecha_creacion']