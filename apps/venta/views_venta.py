from django.shortcuts import render
from rest_framework import viewsets
from django.db import transaction
from apps.venta.serializer import VentaSerializer, DetalleVentaSerializer, EstadoVentaSerializer, MetodoPagoSerializer
from apps.venta.models import Venta, DetalleVenta, EstadoVenta, MetodoPago

class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta


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
