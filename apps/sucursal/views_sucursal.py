from django.shortcuts import render
from rest_framework import viewsets
from django.db import transaction
from apps.entidad.serializer import EntidadSerializer
from apps.sucursal.serializer import SucursalSerializer, EmpleadoSerializer, TurnoSerializer
from apps.sucursal.models import Sucursal, Empleado, Turno

class SucursalViewSet(viewsets.ModelViewSet):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()
    modelo = Sucursal


class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    modelo = Empleado


    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])

        cliente = EmpleadoSerializer.json_to_obj(request.data)

        entidad.save()
        cliente.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        cliente_ser = EmpleadoSerializer.obj_to_json(cliente)

        cliente_ser['entidad'] = entidad_ser

        return Response(cliente_ser, status=200)

    def update(self, request, *args, **kwargs):

        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])

        proveedor = EmpleadoSerializer.json_to_obj(request.data)

        entidad.save()
        proveedor.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = EmpleadoSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)

class TurnoViewSet(viewsets.ModelViewSet):
    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()
    modelo = Turno
