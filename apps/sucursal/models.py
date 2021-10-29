from base.modelo_base import ModeloBase, models

# Create your models here.
class Sucursal(ModeloBase):
    telefono = models.CharField(max_length=8, null=True)
    direccion = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'sucursal'
        verbose_name = 'sucursal'

class Empleado(ModeloBase):
    entidad_id = models.IntegerField()
    fecha_ingreso = models.DateField()
    flg_activo = models.IntegerField()

    class Meta:
        db_table = 'empleado'
        verbose_name = 'empleado'

class Turno(ModeloBase):
    sucursal_id = models.IntegerField()
    empleado_id = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    class Meta:
        db_table = 'turno'
        verbose_name = 'turno'
