from base.serializer_base import SerializerBase
from apps.sucursal.models import Sucursal, Empleado, Turno


class SucursalSerializer(SerializerBase):
    class Meta:
        model = Sucursal
        fields = '__all__'


class EmpleadoSerializer(SerializerBase):
    class Meta:
        model = Empleado
        fields = '__all__'


class TurnoSerializer(SerializerBase):
    class Meta:
        model = Turno
        fields = '__all__'
