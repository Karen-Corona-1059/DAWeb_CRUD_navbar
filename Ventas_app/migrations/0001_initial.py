# Generated by Django 5.1.2 on 2024-11-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('id_producto', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('id_sucursal', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
                ('Total', models.FloatField()),
                ('Fecha', models.DateTimeField()),
            ],
        ),
    ]
