from base.serializer_base import SerializerBase
from apps.entidad.models import Entidad, Cliente, Proveedor


class EntidadSerializer(SerializerBase):
    class Meta:
        model = Entidad
        fields = '__all__'


class ClienteSerializer(SerializerBase):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProveedorSerializer(SerializerBase):
    class Meta:
        model = Proveedor
        fields = '__all__'
