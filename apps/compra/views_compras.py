from django.shortcuts import render
from rest_framework import viewsets
from django.db import transaction
from apps.compra.serializer import CompraSerializer, DetalleCompraSerializer, EstadoCompraSerializer
from apps.compra.models import Compra, DetalleCompra, EstadoCompra

class CompraViewSet(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    modelo = Compra


class DetalleCompraViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleCompraSerializer
    queryset = DetalleCompra.objects.all()
    modelo = DetalleCompra


class EstadoCompraViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoCompraSerializer
    queryset = EstadoCompra.objects.all()
    modelo = EstadoCompra


