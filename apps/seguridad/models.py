from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    usuario = models.CharField(max_length=15)
    password = models.TextField()
    flg_activo = models.BooleanField()
    rol_id = models.IntegerField()

    class Meta:
        db_table = 'usuarios'


class Rol(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'roles'
        ordering = ['id']


class Operacion(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'operaciones'
        ordering = ['id']


class Acceso(models.Model):
    rol_id = models.IntegerField()
    operacion_id = models.IntegerField()

    class Meta:
        db_table = 'rol_accesos'
        ordering = ['id']
