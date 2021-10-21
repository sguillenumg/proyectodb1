from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User
from .models import Usuario, Acceso

class SeguridadViewSet(ViewsetBase):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['usuario'])
        
        if not user.check_password(request.data['password']):
            return Response("Usuario y contraseña no coinciden", status=400)

        usuario = Usuario.objects.get(pk=user.id)
        accesos = Acceso.objects.filter(rol_id=usuario.rol_id).values()

        res = {
            usuario: usuario.usuario,
            nombre: usuario.nombre,
            apellido: usuario.apellido,
            accesos: accesos
        }

        return Response(res, status=200)
