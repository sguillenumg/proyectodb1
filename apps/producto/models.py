from base.modelo_base import ModeloBase, models

# Create your models here.
class Producto(ModeloBase):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'producto'
        verbose_name = 'producto'

class Inventario(ModeloBase):
    producto_id = models.IntegerField()
    sucursal_id = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'inventario'
        verbose_name = 'inventario'

