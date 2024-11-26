
from django.db import models

class Ventas(models.Model):
    id_venta = models.CharField(max_length=10, primary_key=True)  # O un campo que uses como PK
    id_producto = models.IntegerField()
    id_cliente = models.IntegerField()
    id_sucursal = models.IntegerField()
    id_empleado = models.IntegerField()
    Total = models.FloatField()
    Fecha = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):

        return self.nombre