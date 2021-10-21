from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from apps.entidad.serializer import EntidadSerializer
from apps.sucursal.serializer import SucursalSerializer, EmpleadoSerializer, TurnoSerializer
from apps.sucursal.models import Sucursal, Empleado, Turno

class SucursalViewSet(ViewsetBase):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()
    modelo = Sucursal


class EmpleadoViewSet(ViewsetBase):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    modelo = Empleado


    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(1, None, None)

        empleado = EmpleadoSerializer.json_to_obj(request.data)
        empleado.entidad_id = entidad.id
        empleado.save(1, None, None)

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        empleado_ser = EmpleadoSerializer.obj_to_json(empleado)

        empleado_ser['entidad'] = entidad_ser

        return Response(empleado_ser, status=200)

    def update(self, request, *args, **kwargs):

        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(1, None, None)

        empleado = EmpleadoSerializer.json_to_obj(request.data)
        empleado.entidad_id = entidad.id
        empleado.save(1, None, None)

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        empleado_ser = EmpleadoSerializer.obj_to_json(empleado)

        empleado_ser['entidad'] = entidad_ser

        return Response(empleado_ser, status=200)

class TurnoViewSet(ViewsetBase):
    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()
    modelo = Turno
