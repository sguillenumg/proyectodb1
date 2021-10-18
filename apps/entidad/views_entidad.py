from django.shortcuts import render
from rest_framework import viewsets
from django.db import transaction
from apps.entidad.serializer import EntidadSerializer
from apps.entidad.models import Entidad

class EntidadViewSet(viewsets.ModelViewSet):
    serializer_class = EntidadSerializer
    queryset = Entidad.objects.all()
    modelo = Entidad
