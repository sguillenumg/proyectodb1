from base.modelo_base import ModeloBase, models

# Create your models here.
class Venta(ModeloBase):
    cliente_id = models.IntegerField()
    emp_cajero_id = models.IntegerField()
    sucursal_id = models.IntegerField()
    metodo_pago_id = models.IntegerField()
    estado_venta_id = models.IntegerField()
    documento = models.CharField(max_length=15)
    fecha = models.DateField()
    direccion_entrega = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'ventas'
        verbose_name = 'ventas'

class DetalleVenta(ModeloBase):
    venta_id = models.IntegerField()
    producto_id = models.IntegerField()
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'venta_detalles'
        verbose_name = 'venta_detalles'


class EstadoVenta(ModeloBase):
    descripcion = models.CharField(max_length=15)

    class Meta:
        db_table = 'venta_estados'
        verbose_name = 'venta_estados'


class MetodoPago(ModeloBase):
    descripcion = models.CharField(max_length=15)

    class Meta:
        db_table = 'metodos_pago'
        verbose_name = 'metodos_pago'
