from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from apps.venta.serializer import VentaSerializer, DetalleVentaSerializer, EstadoVentaSerializer, MetodoPagoSerializer
from apps.venta.models import Venta, DetalleVenta, EstadoVenta, MetodoPago
from apps.producto.models import Inventario
from apps.producto.serializer import InventarioSerializer

class VentaViewSet(ViewsetBase):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    def create(self, request, *args, **kwargs):
        detalles = request.data['detalles']

        del(request.data['detalles'])

        venta = VentaSerializer.json_to_obj(request.data)
        venta.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, request.data)

        for det in detalles:
            detalle = DetalleVentaSerializer.json_to_obj(det)
            detalle.venta_id = venta.id
            detalle.save(
                request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, det, venta.id)

            try:
                inventario = Inventario.objects.get(sucursal_id=venta.sucursal_id, producto_id=detalle.producto_id)
                inv_old_new = InventarioSerializer.obj_to_json(inventario)
                inventario.cantidad = inventario.cantidad - detalle.cantidad
                inv_new = InventarioSerializer.obj_to_json(inventario)

                if inventario.cantidad < 0:
                    return Response("Cantidad insuficiente del producto: {}".format(detalle.producto_id), status=400)

                inventario.save(
                    request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old_new, inv_new)
            except Inventario.DoesNotExist:
                return Response("Cantidad insuficiente del producto: {}".format(detalle.producto_id), status=400)

        return Response(venta.id, status=200)

    def update(self, request, *args, **kwargs):

        detalles = request.data['detalles']

        del(request.data['detalles'])

        venta = VentaSerializer.json_to_obj(request.data)
        venta.save(
            request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, request.data, request.data)

        det_actuales = list(DetalleVenta.objects.filter(venta_id=venta.id))
        for det in det_actuales:
            inventario = Inventario.objects.get(
                sucursal_id=venta.sucursal_id, producto_id=det.producto_id)
            inv_old = InventarioSerializer.obj_to_json(inventario)
            inventario.cantidad = inventario.cantidad + det.cantidad
            inv_new = InventarioSerializer.obj_to_json(inventario)
            inventario.save(
                request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old, inv_new)

            det.delete(
                request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, det, venta.id)

        for det in detalles:
            detalle = DetalleVentaSerializer.json_to_obj(det)
            detalle.venta_id = venta.id
            detalle.save(
                request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, det)

            inventario = Inventario.objects.get(
                sucursal_id=venta.sucursal_id, producto_id=detalle.producto_id)
            inv_old = InventarioSerializer.obj_to_json(inventario)
            inventario.cantidad = inventario.cantidad - detalle.cantidad
            inv_new = InventarioSerializer.obj_to_json(inventario)
            inventario.save(
                request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old, inv_new)

        return Response(venta.id, status=200)


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
