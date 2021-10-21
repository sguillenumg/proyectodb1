from django.db import models

class ModeloBase(models.Model):

    def save(self, usuario_id, obj_old, obj_new):
        super().save()

    def delete(self, usuario_id, obj_old):
        
        super().delete()

    class Meta:
        abstract = True
