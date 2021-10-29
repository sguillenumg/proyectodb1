from base.modelo_base import ModeloBase, models

# Create your models here.
class Entidad(ModeloBase):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dpi = models.CharField(max_length=15, null=True)
    nit = models.CharField(max_length=10)
    telefono = models.CharField(max_length=8, null=True)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=200, null=True)
    correo = models.CharField(max_length=25, null=True)

    class Meta:
        db_table = 'entidad'
        verbose_name = 'entidad'

class Cliente(ModeloBase):
    entidad_id = models.IntegerField()
    puntos = models.IntegerField(null=True)

    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'

class Proveedor(ModeloBase):
    entidad_id = models.IntegerField()

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'proveedor'
