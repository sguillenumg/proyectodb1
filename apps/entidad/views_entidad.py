from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from apps.entidad.serializer import EntidadSerializer, ClienteSerializer, ProveedorSerializer
from apps.entidad.models import Entidad, Cliente, Proveedor


class EntidadViewSet(ViewsetBase):
    serializer_class = EntidadSerializer
    queryset = Entidad.objects.all()
    modelo = Entidad

class ClienteViewSet(ViewsetBase):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    modelo = Cliente

    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, request.data)

        cliente = ClienteSerializer.json_to_obj(request.data)
        cliente.entidad_id = entidad.id
        cliente.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, ClienteSerializer.obj_to_json(cliente))

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        cliente_ser = ClienteSerializer.obj_to_json(cliente)

        cliente_ser['entidad'] = entidad_ser

        return Response(cliente_ser, status=200)

    def update(self, request, *args, **kwargs):
    
        actual = self.get_object()
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, request.data['entidad'], request.data['entidad'])

        cliente = ClienteSerializer.json_to_obj(request.data)
        cliente.entidad_id = entidad.id
        cliente.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, request.data, request.data)

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        cliente_ser = ClienteSerializer.obj_to_json(cliente)

        cliente_ser['entidad'] = entidad_ser

        return Response(cliente_ser, status=200)



class ProveedorViewSet(ViewsetBase):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()
    modelo = Proveedor

    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, request.data)

        proveedor = ProveedorSerializer.json_to_obj(request.data)
        proveedor.entidad_id = entidad.id
        proveedor.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, request.data)

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = ProveedorSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)

    def update(self, request, *args, **kwargs):

        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, request.data['entidad'], request.data['entidad'])

        proveedor = ProveedorSerializer.json_to_obj(request.data)
        proveedor.entidad_id = entidad.id
        proveedor.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, request.data, request.data)

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = ProveedorSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)
