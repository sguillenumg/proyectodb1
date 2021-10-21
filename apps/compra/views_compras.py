from django.shortcuts import render
from base.viewset_base import ViewsetBase
from django.db import transaction
from apps.compra.serializer import CompraSerializer, DetalleCompraSerializer, EstadoCompraSerializer
from apps.compra.models import Compra, DetalleCompra, EstadoCompra

class CompraViewSet(ViewsetBase):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    modelo = Compra


class DetalleCompraViewSet(ViewsetBase):
    serializer_class = DetalleCompraSerializer
    queryset = DetalleCompra.objects.all()
    modelo = DetalleCompra


class EstadoCompraViewSet(ViewsetBase):
    serializer_class = EstadoCompraSerializer
    queryset = EstadoCompra.objects.all()
    modelo = EstadoCompra


