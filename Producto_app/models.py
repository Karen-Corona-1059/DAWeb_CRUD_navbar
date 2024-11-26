from django.db import models

# Create your models here.
class Productos(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    precio = models.FloatField()
    cantidad=models.SmallIntegerField()
    descripcion=models.CharField(max_length=100)
    categoria=models.CharField(max_length=20)
    id_provedor=models.SmallIntegerField()
    def __str__(self):

        return self.nombre