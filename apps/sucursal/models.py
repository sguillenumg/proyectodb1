from django.db import models

# Create your models here.
class Sucursal(models.Model):
    telefono = models.CharField(max_length=8, null=True)
    direccion = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'sucursales'
        verbose_name = 'sucursales'

class Empleado(models.Model):
    entidad_id = models.IntegerField()
    fecha_ingreso = models.DateField()
    flg_activo = models.IntegerField()

    class Meta:
        db_table = 'empleados'
        verbose_name = 'empleados'

class Turno(models.Model):
    sucursal_id = models.IntegerField()
    empleado_id = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    class Meta:
        db_table = 'turnos'
        verbose_name = 'turnos'
