from base.serializer_base import SerializerBase
from apps.venta.models import Venta, DetalleVenta, EstadoVenta, MetodoPago


class VentaSerializer(SerializerBase):
    class Meta:
        model = Venta
        fields = '__all__'


class DetalleVentaSerializer(SerializerBase):
    class Meta:
        model = DetalleVenta
        fields = '__all__'


class EstadoVentaSerializer(SerializerBase):
    class Meta:
        model = EstadoVenta
        fields = '__all__'


class MetodoPagoSerializer(SerializerBase):
    class Meta:
        model = MetodoPago
        fields = '__all__'

