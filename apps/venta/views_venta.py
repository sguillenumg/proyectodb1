from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.db import transaction
from apps.venta.serializer import VentaSerializer, DetalleVentaSerializer, EstadoVentaSerializer, MetodoPagoSerializer
from apps.venta.models import Venta, DetalleVenta, EstadoVenta, MetodoPago
from apps.producto.models import Inventario

class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    def create(self, request, *args, **kwargs):
        detalles = request.data['detalles']

        del(request.data['detalles'])

        venta = VentaSerializer.json_to_obj(request.data)
        venta.save()

        for det in detalles:
            detalle = DetalleVentaSerializer.json_to_obj(det)
            detalle.save()

            inventario = Inventario.objects.get(sucursal_id=venta.sucursal_id, producto_id=detalle.producto_id)
            inventario.cantidad = inventario.cantidad - 1
            inventario.save()

        return Response(proveedor_ser, status=200)

    def update(self, request, *args, **kwargs):

        entidad = EntidadSerializer.json_to_obj(request.data['entidad'])

        proveedor = ProveedorSerializer.json_to_obj(request.data)

        entidad.save()
        proveedor.save()

        entidad_ser = EntidadSerializer.obj_to_json(entidad)
        proveedor_ser = ProveedorSerializer.obj_to_json(proveedor)

        proveedor_ser['entidad'] = entidad_ser

        return Response(proveedor_ser, status=200)


class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSerializer
    queryset = DetalleVenta.objects.all()
    modelo = DetalleVenta


class EstadoVentaViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoVentaSerializer
    queryset = EstadoVenta.objects.all()
    modelo = EstadoVenta


class MetodoPagoViewSet(viewsets.ModelViewSet):
    serializer_class = MetodoPagoSerializer
    queryset = MetodoPago.objects.all()
    modelo = MetodoPago
