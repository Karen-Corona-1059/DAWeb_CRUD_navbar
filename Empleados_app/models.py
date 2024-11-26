from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    Direccion=models.CharField(max_length=100)
    rfc=models.CharField(max_length=100)
    Sueldo=models.IntegerField()
    Puesto=models.CharField(max_length=100)
    HorarioE=models.TimeField( auto_now=False, auto_now_add=False)
    HorarioS=models.TimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.nombre