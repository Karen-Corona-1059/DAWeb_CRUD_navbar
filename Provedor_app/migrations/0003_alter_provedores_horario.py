# Generated by Django 5.1 on 2024-11-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Provedor_app', '0002_alter_provedores_telefono_alter_provedores_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedores',
            name='horario',
            field=models.CharField(max_length=20),
        ),
    ]