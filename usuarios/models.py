from django.db import models

class Usuario(models.Model):
    # Nombre de usuario único para evitar cuentas duplicadas
    username = models.CharField(max_length=50, unique=True)
    # Correo electrónico único para evitar registros duplicados
    email = models.EmailField(unique=True)
    # Contraseña almacenada de forma segura mediante hash
    password = models.CharField(max_length=128)
    # Cantidad de intentos incorrectos de inicio de sesión
    intentos = models.IntegerField(default=0)
    # Indica si la cuenta quedó bloqueada por superar los 3 intentos
    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        return self.username