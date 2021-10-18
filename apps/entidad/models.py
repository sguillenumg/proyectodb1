from django.db import models

# Create your models here.
class Entidad(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dpi = models.CharField(max_length=15, null=True)
    nit = models.CharField(max_length=10)
    telefono = models.CharField(max_length=8, null=True)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=200, null=True)
    correo = models.CharField(max_length=25, null=True)

    class Meta:
        db_table = 'entidades'
        verbose_name = 'entidades'

class Cliente(models.Model):
    entidad_id = models.IntegerField()
    puntos = models.IntegerField(null=True)

    class Meta:
        db_table = 'clientes'
        verbose_name = 'clientes'

class Proveedor(models.Model):
    entidad_id = models.IntegerField()

    class Meta:
        db_table = 'proveedores'
        verbose_name = 'proveedores'
