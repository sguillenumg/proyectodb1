from django.shortcuts import render
from base.viewset_base import ViewsetBase
from django.db import transaction
from apps.producto.serializer import ProductoSerializer, InventarioSerializer
from apps.producto.models import Producto, Inventario

class ProductoViewSet(ViewsetBase):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    modelo = Producto


class InventarioViewSet(ViewsetBase):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
    modelo = Inventario
