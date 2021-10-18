from django.db import models

# Create your models here.
class Compra(models.Model):
    proveedor_id = models.IntegerField()
    sucursal_id = models.IntegerField()
    estado_compra_id = models.IntegerField()
    documento = models.CharField(max_length=15)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'compras'
        verbose_name = 'compras'

class DetalleCompra(models.Model):
    compra_id = models.IntegerField()
    producto_id = models.IntegerField()
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'compra_detalles'
        verbose_name = 'compra_detalles'


class EstadoCompra(models.Model):
    descripcion = models.CharField(max_length=15)

    class Meta:
        db_table = 'compra_estados'
        verbose_name = 'compra_estados'

