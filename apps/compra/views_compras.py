from django.shortcuts import render
from base.viewset_base import ViewsetBase
from django.db import transaction
from apps.compra.serializer import CompraSerializer, DetalleCompraSerializer, EstadoCompraSerializer
from apps.compra.models import Compra, DetalleCompra, EstadoCompra
from apps.producto.models import Inventario
from rest_framework.response import Response

class CompraViewSet(ViewsetBase):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    modelo = Compra


    def create(self, request, *args, **kwargs):
        detalles = request.data['detalles']

        del(request.data['detalles'])

        compra = CompraSerializer.json_to_obj(request.data)
        compra.save(1, None, None)

        for det in detalles:
            detalle = DetalleCompraSerializer.json_to_obj(det)
            detalle.compra_id = compra.id
            detalle.save(1, None, None)

            try:
                inventario = Inventario.objects.get(sucursal_id=compra.sucursal_id, producto_id=detalle.producto_id)
                inventario.cantidad = inventario.cantidad + detalle.cantidad
                inventario.save(1, None, None)

            except Inventario.DoesNotExist:
                inventario = Inventario()
                inventario.sucursal_id = compra.sucursal_id
                inventario.producto_id = detalle.producto_id
                inventario.cantidad = detalle.cantidad
                inventario.save(1,None,None)

        return Response(compra.id, status=200)

    def update(self, request, *args, **kwargs):

        detalles = request.data['detalles']

        del(request.data['detalles'])

        compra = CompraSerializer.json_to_obj(request.data)
        compra.save(1, None, None)

        det_actuales = list(DetalleCompra.objects.filter(compra_id=compra.id))
        for det in det_actuales:
            inventario = Inventario.objects.get(
                sucursal_id=compra.sucursal_id, producto_id=det.producto_id)
            inventario.cantidad = inventario.cantidad - det.cantidad
            inventario.save(1, None, None)

            det.delete()

        for det in detalles:
            detalle = DetalleCompraSerializer.json_to_obj(det)
            detalle.compra_id = compra.id
            detalle.save(1, None, None)

            try:
                inventario = Inventario.objects.get(sucursal_id=compra.sucursal_id, producto_id=detalle.producto_id)
                inventario.cantidad = inventario.cantidad + detalle.cantidad
                inventario.save(1, None, None)

            except Inventario.DoesNotExist:
                inventario = Inventario()
                inventario.sucursal_id = compra.sucursal_id
                inventario.producto_id = detalle.producto_id
                inventario.cantidad = detalle.cantidad
                inventario.save(1,None,None)

        return Response(compra.id, status=200)

class DetalleCompraViewSet(ViewsetBase):
    serializer_class = DetalleCompraSerializer
    queryset = DetalleCompra.objects.all()
    modelo = DetalleCompra


class EstadoCompraViewSet(ViewsetBase):
    serializer_class = EstadoCompraSerializer
    queryset = EstadoCompra.objects.all()
    modelo = EstadoCompra


