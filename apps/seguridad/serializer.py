from base.serializer_base import SerializerBase
from .models import Rol, Acceso, Operacion, Usuario


class UsuarioSerializer(SerializerBase):
    class Meta:
        model = Usuario
        fields = '__all__' 


class RolSerializer(SerializerBase):
    class Meta:
        model = Rol
        fields = '__all__'


class AccesoSerializer(SerializerBase):
    class Meta:
        model = Acceso
        fields = '__all__'


class OperacionSerializer(SerializerBase):
    class Meta:
        model = Operacion
        fields = '__all__'


