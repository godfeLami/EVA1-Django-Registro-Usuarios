from django.db import models

class Producto(models.Model):
    
    # Nombre de la herramienta ninja
    nombre = models.CharField(max_length=100)
    
    # Aldea que representa la marca
    marca = models.CharField(max_length=100)
    
    # Precio de la herramienta ninja
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre