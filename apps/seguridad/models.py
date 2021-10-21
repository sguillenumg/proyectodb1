from base.modelo_base import ModeloBase


class Usuario(ModeloBase):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    usuario = models.CharField(max_length=15)
    password = models.TextField()
    flg_activo = models.BooleanField()
    rol_id = models.IntegerField()

    class Meta:
        db_table = 'usuarios'


class Rol(ModeloBase):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'roles'
        ordering = ['id']


class Operacion(ModeloBase):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'operaciones'
        ordering = ['id']


class Acceso(ModeloBase):
    rol_id = models.IntegerField()
    operacion_id = models.IntegerField()

    class Meta:
        db_table = 'rol_accesos'
        ordering = ['id']
