# Generated by Django 5.1.3 on 2024-11-15 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedores',
            fields=[
                ('id_provedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('Telefono', models.IntegerField()),
                ('sucursal', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('horario', models.TimeField()),
                ('id_producto', models.SmallIntegerField()),
            ],
        ),
    ]
