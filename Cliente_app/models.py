from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    Telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=30)
    fecha=models.DateField( auto_now=False, auto_now_add=False)
    direccion=models.CharField(max_length=20)
    def __str__(self):

        return self.nombre