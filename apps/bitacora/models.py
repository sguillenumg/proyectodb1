from django.db import models

class Bitacora(models.Model):
    usuario_id = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=10)
    fecha = models.DateTimeField()
    tabla = models.CharField(max_length=20)
    registro_id = models.IntegerField()
    padre_id = models.IntegerField(null=True)
    obj_old = models.CharField(max_length=2000)
    obj_new = models.CharField(max_length=2000)

    class Meta:
        db_table = 'bitacora'
