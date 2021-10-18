from django.shortcuts import render
from rest_framework import viewsets
from django.db import transaction
from apps.producto.serializer import ProductoSerializer, InventarioSerializer
from apps.producto.models import Producto, Inventario

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    modelo = Producto


class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
    modelo = Inventario
