from base.serializer_base import SerializerBase
from apps.compra.models import Compra, DetalleCompra, EstadoCompra


class CompraSerializer(SerializerBase):
    class Meta:
        model = Compra
        fields = '__all__'


class DetalleCompraSerializer(SerializerBase):
    class Meta:
        model = DetalleCompra
        fields = '__all__'


class EstadoCompraSerializer(SerializerBase):
    class Meta:
        model = EstadoCompra
        fields = '__all__'


