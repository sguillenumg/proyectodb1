from base.modelo_base import ModeloBase, models


# Create your models here.
class Compra(ModeloBase):
    proveedor_id = models.IntegerField()
    sucursal_id = models.IntegerField()
    estado_compra_id = models.IntegerField()
    documento = models.CharField(max_length=15)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'compra'
        verbose_name = 'compra'

class DetalleCompra(ModeloBase):
    compra_id = models.IntegerField()
    producto_id = models.IntegerField()
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'detalle_compra'
        verbose_name = 'detalle_compra'


class EstadoCompra(ModeloBase):
    descripcion = models.CharField(max_length=15)

    class Meta:
        db_table = 'estado_compra'
        verbose_name = 'estado_compra'

