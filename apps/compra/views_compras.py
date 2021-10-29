from django.shortcuts import render
from base.viewset_base import ViewsetBase
from django.db import transaction
from apps.compra.serializer import CompraSerializer, DetalleCompraSerializer, EstadoCompraSerializer
from apps.compra.models import Compra, DetalleCompra, EstadoCompra
from apps.producto.models import Inventario
from apps.producto.serializer import InventarioSerializer
from rest_framework.response import Response

class CompraViewSet(ViewsetBase):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    modelo = Compra


    def create(self, request, *args, **kwargs):
        detalles = request.data['detalles']

        del(request.data['detalles'])

        compra = CompraSerializer.json_to_obj(request.data)
        compra.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, request.data)

        for det in detalles:
            detalle = DetalleCompraSerializer.json_to_obj(det)
            detalle.compra_id = compra.id
            detalle.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, det, compra.id)

            try:
                inventario = Inventario.objects.get(sucursal_id=compra.sucursal_id, producto_id=detalle.producto_id)
                inv_old_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.cantidad = inventario.cantidad + detalle.cantidad
                inv_new_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old_ser, inv_new_ser)

            except Inventario.DoesNotExist:
                inventario = Inventario()
                inventario.sucursal_id = compra.sucursal_id
                inventario.producto_id = detalle.producto_id
                inventario.cantidad = detalle.cantidad
                inv_new_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, inv_new_ser)

        return Response(compra.id, status=200)

    def update(self, request, *args, **kwargs):

        actual = self.get_object()
        actual_ser = CompraSerializer.obj_to_json(actual)
        detalles = request.data['detalles']

        del(request.data['detalles'])

        compra = CompraSerializer.json_to_obj(request.data)
        compra.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, actual_ser, request.data)

        det_actuales = list(DetalleCompra.objects.filter(compra_id=compra.id))
        for det in det_actuales:
            inventario = Inventario.objects.get(sucursal_id=compra.sucursal_id, producto_id=det.producto_id)
            inv_old_ser = InventarioSerializer.obj_to_json(inventario)
            inventario.cantidad = inventario.cantidad - det.cantidad
            inv_new_ser = InventarioSerializer.obj_to_json(inventario)
            inventario.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old_ser, inv_new_ser)

            det_old = DetalleCompraSerializer.obj_to_json(det)
            det.delete(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, det_old, compra.id)

        for det in detalles:
            detalle = DetalleCompraSerializer.json_to_obj(det)
            detalle.compra_id = compra.id
            detalle.save(request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, det, compra.id)

            try:
                inventario = Inventario.objects.get(sucursal_id=compra.sucursal_id, producto_id=detalle.producto_id)
                inv_old_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.cantidad = inventario.cantidad + detalle.cantidad
                inv_new_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.save(
                    request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, inv_old_ser, inv_new_ser)

            except Inventario.DoesNotExist:
                inventario = Inventario()
                inventario.sucursal_id = compra.sucursal_id
                inventario.producto_id = detalle.producto_id
                inventario.cantidad = detalle.cantidad
                inv_new_ser = InventarioSerializer.obj_to_json(inventario)
                inventario.save(
                    request.query_params['usuario_id'] if 'usuario_id' in request.query_params else -1, None, inv_new_ser)

        return Response(compra.id, status=200)

class DetalleCompraViewSet(ViewsetBase):
    serializer_class = DetalleCompraSerializer
    queryset = DetalleCompra.objects.all()
    modelo = DetalleCompra


class EstadoCompraViewSet(ViewsetBase):
    serializer_class = EstadoCompraSerializer
    queryset = EstadoCompra.objects.all()
    modelo = EstadoCompra


