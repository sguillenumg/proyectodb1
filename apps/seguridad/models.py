from base.modelo_base import ModeloBase, models


class Usuario(ModeloBase):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    usuario = models.CharField(max_length=15)
    password = models.TextField()
    flg_activo = models.BooleanField()

    class Meta:
        db_table = 'usuarios'


class Rol(ModeloBase):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'roles'


class Operacion(ModeloBase):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'operaciones'


class Acceso(ModeloBase):
    rol_id = models.IntegerField()
    operacion_id = models.IntegerField()

    class Meta:
        db_table = 'rol_accesos'


class RolUsuario(ModeloBase):
    rol_id = models.IntegerField()
    usuario_id = models.IntegerField()

    class Meta:
        db_table = 'rol_usuarios'
