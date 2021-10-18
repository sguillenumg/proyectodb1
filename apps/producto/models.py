from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'productos'
        verbose_name = 'productos'

class Inventario(models.Model):
    producto_id = models.IntegerField()
    sucursal_id = models.IntegerField()
    puntos = models.IntegerField(null=True)

    class Meta:
        db_table = 'inventarios'
        verbose_name = 'inventarios'

