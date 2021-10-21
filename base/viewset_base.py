import base64
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from django.db import transaction

class ViewsetBase(viewsets.ModelViewSet):

    @transaction.atomic
    def create(self, request, res_obj=False, *args, **kwargs):

        obj = self.get_serializer().json_to_obj(request.data)
        obj.save(request, None, request.data)

        return Response(self.get_serializer().obj_to_json(obj), 200)

    @transaction.atomic
    def update(self, request, res_obj=False, *args, **kwargs):
        actual = self.get_object()
        obj = self.get_serializer().json_to_obj(request.data)

        obj.save(request, self.get_serializer().obj_to_json(actual), request.data)

        return Response(self.get_serializer().obj_to_json(obj), 200)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete(request, self.get_serializer().obj_to_json(obj))

        return Response(True, 200)