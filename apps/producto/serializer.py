from base.serializer_base import SerializerBase
from apps.producto.models import Producto, Inventario


class ProductoSerializer(SerializerBase):
    class Meta:
        model = Producto
        fields = '__all__'


class InventarioSerializer(SerializerBase):
    class Meta:
        model = Inventario
        fields = '__all__'

