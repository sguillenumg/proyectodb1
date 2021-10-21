from django.db import models
from apps.bitacora.models import Bitacora
from datetime import date

class ModeloBase(models.Model):

    def save(self, usuario_id, obj_old=None, obj_new=None, padre_id=None):
        super().save()

        bitacora = Bitacora()
        bitacora.usuario_id = usuario_id
        bitacora.tipo_movimiento = 'INSERT' if obj_old is None else 'UPDATE'
        bitacora.fecha = date.today()
        bitacora.tabla = getattr(self._meta, 'verbose_name', 'Error')
        bitacora.registro_id = getattr(self, 'id', '-1')
        bitacora.padre_id = padre_id
        bitacora.obj_old = obj_old
        bitacora.obj_new = obj_new
        bitacora.save()

    def delete(self, usuario_id, obj_old, padre_id=None):
        bitacora = Bitacora()
        bitacora.usuario_id = usuario_id
        bitacora.tipo_movimiento = 'DELETE'
        bitacora.fecha = date.today()
        bitacora.tabla = getattr(self._meta, 'verbose_name', 'Error')
        bitacora.registro_id = obj_old['id']
        bitacora.padre_id = padre_id
        bitacora.obj_old = obj_old
        bitacora.obj_new = None
        bitacora.save()
        super().delete()

    class Meta:
        abstract = True
