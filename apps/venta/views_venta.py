from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from apps.venta.serializer import VentaSerializer, DetalleVentaSerializer, EstadoVentaSerializer, MetodoPagoSerializer
from apps.venta.models import Venta, DetalleVenta, EstadoVenta, MetodoPago
from apps.producto.models import Inventario

class VentaViewSet(ViewsetBase):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    def create(self, request, *args, **kwargs):
        detalles = request.data['detalles']

        del(request.data['detalles'])

        venta = VentaSerializer.json_to_obj(request.data)
        venta.save(1, None, None)

        for det in detalles:
            detalle = DetalleVentaSerializer.json_to_obj(det)
            detalle.venta_id = venta.id
            detalle.save(1, None, None)

            try
                inventario = Inventario.objects.get(sucursal_id=venta.sucursal_id, producto_id=detalle.producto_id)
                inventario.cantidad = inventario.cantidad - detalle.cantidad

                if cantidad < 0:
                    return Response("Cantidad insuficiente del producto: {}".format(detalle.producto_id), status=400)

                inventario.save(1, None, None)
            except Inventario.DoesNotExist:
                return Response("Cantidad insuficiente del producto: {}".format(detalle.producto_id), status=400)

        return Response(proveedor_ser, status=200)

    def update(self, request, *args, **kwargs):

        detalles = request.data['detalles']

        del(request.data['detalles'])

        venta = VentaSerializer.json_to_obj(request.data)
        venta.save(1, None, None)

        det_actuales = list(DetalleVenta.objects.filter(venta_id=venta.id))
        for det in det_actuales:
            inventario = Inventario.objects.get(
                sucursal_id=venta.sucursal_id, producto_id=det.producto_id)
            inventario.cantidad = inventario.cantidad + det.cantidad
            inventario.save(1, None, None)

            det.delete()

        for det in detalles:
            detalle = DetalleVentaSerializer.json_to_obj(det)
            detalle.venta_id = venta.id
            detalle.save(1, None, None)

            inventario = Inventario.objects.get(
                sucursal_id=venta.sucursal_id, producto_id=detalle.producto_id)
            inventario.cantidad = inventario.cantidad - detalle.cantidad
            inventario.save(1, None, None)

        return Response(proveedor_ser, status=200)


class DetalleVentaViewSet(ViewsetBase):
    serializer_class = DetalleVentaSerializer
    queryset = DetalleVenta.objects.all()
    modelo = DetalleVenta


class EstadoVentaViewSet(ViewsetBase):
    serializer_class = EstadoVentaSerializer
    queryset = EstadoVenta.objects.all()
    modelo = EstadoVenta


class MetodoPagoViewSet(ViewsetBase):
    serializer_class = MetodoPagoSerializer
    queryset = MetodoPago.objects.all()
    modelo = MetodoPago
