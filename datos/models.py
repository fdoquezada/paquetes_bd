from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    pais = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.PositiveIntegerField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre    