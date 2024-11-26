from django.db import models

# Create your models here.

class Provedores(models.Model):
    id_provedor=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    Telefono=models.CharField(max_length=10)
    sucursal=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    HorarioE=models.TimeField( auto_now=False, auto_now_add=False)
    HorarioS=models.TimeField( auto_now=False, auto_now_add=False)
    id_producto=models.SmallIntegerField()
    def __str__(self):

        return self.nombre