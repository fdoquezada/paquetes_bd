from django.contrib import admin
from .models import Usuario, Producto


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'pais')
    list_filter = ('pais',)
    search_fields = ('nombre', 'apellido')
    orderings = ('pais',)
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_de_creacion')   
    

# Register your models here.
