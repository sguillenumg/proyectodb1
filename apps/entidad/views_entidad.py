from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.db import transaction
from apps.entidad.serializer import EntidadSerializer, ClienteSerializer, ProveedorSerializer
from apps.entidad.models import Entidad, Cliente, Proveedor

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    modelo = Cliente

    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save()

        cliente = ClienteSerializer.json_to_obj(request.data)
        cliente.entidad_id = entidad.id
        cliente.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        cliente_ser = ClienteSerializer.obj_to_json(cliente)

        cliente_ser['entidad'] = entidad_ser

        return Response(cliente_ser, status=200)

    def update(self, request, *args, **kwargs):
    
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save()

        cliente = ClienteSerializer.json_to_obj(request.data)
        cliente.entidad_id = entidad.id
        cliente.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        cliente_ser = ClienteSerializer.obj_to_json(cliente)

        cliente_ser['entidad'] = entidad_ser

        return Response(cliente_ser, status=200)



class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()
    modelo = Proveedor

    def create(self, request, *args, **kwargs):
        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save()

        proveedor = ProveedorSerializer.json_to_obj(request.data)
        proveedor.entidad_id = entidad.id
        proveedor.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = ProveedorSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)

    def update(self, request, *args, **kwargs):

        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])
        entidad.save()

        proveedor = ProveedorSerializer.json_to_obj(request.data)
        proveedor.entidad_id = entidad.id
        proveedor.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = ProveedorSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)
