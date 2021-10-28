from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User
from .models import Usuario, Acceso, RolUsuario
from apps.venta.serializer import Venta, VentaSerializer

class SeguridadViewSet(ViewsetBase):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        
        if not user.check_password(request.data['password']):
            return Response("Usuario y contraseña no coinciden", status=400)

        lista_accesos = []
        usuario = None
        usuario = Usuario.objects.get(pk=user.id)
        try:
            roles = RolUsuario.objects.filter(usuario_id=usuario.id)
            for rol in roles:
                accesos = Acceso.objects.filter(rol_id=rol.id).values()
                lista_accesos = lista_accesos.append(accesos)
        except:
            pass

        res = {
            'usuario_id': usuario.id if usuario else None,
            'usuario': usuario.usuario if usuario else None,
            'nombre': usuario.nombre if usuario else None,
            'apellido': usuario.apellido if usuario else None,
            'accesos': lista_accesos
        }

        return Response(res, status=200)
