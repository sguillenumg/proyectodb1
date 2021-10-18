from rest_framework import serializers
from rest_framework.exceptions import APIException

class SerializerBase(serializers.ModelSerializer):

    one_to_many = []
    objs_transient = []
    
    validarCampos = False
    
    class Meta:
        abstract = True


    @classmethod
    def json_to_obj(self, json, validarCampos=None):
        ser = self(data=json)
        ser.is_valid()

        if validarCampos is None:
            validarCampos = self.validarCampos;
            
        if validarCampos:
            if ser.errors:
                errores = ''
                for key, valor in ser.errors.items():
                    if valor[0].code == 'null' or valor[0].code == 'required':
                        errores += 'El campo {} es obligatorio. \n'.format(key.replace('_id', '').replace('_', ' '))
                
                raise APIException(errores)

        obj = self.Meta.model(**ser.data)
        obj.id = json['id'] if 'id' in json else None
        obj.creado = json['creado'] if 'creado' in json else None

        for relacion in self.one_to_many:
            nombre_lista = relacion['nombre_lista']
            lista = []
            if nombre_lista in json:
                for det in json[nombre_lista]:
                    obj_det = relacion['ser_detalle'].json_to_obj(det)
                    lista.append(obj_det)

                setattr(obj, nombre_lista, lista)

        return obj

    @classmethod
    def obj_to_json(self, obj):
        json = self(obj).data

        for relacion in self.one_to_many:
            det_json = []
            for det in getattr(obj, relacion['nombre_lista']):
                det_json.append(relacion['ser_detalle'].obj_to_json(det))

            json[relacion['nombre_lista']] = det_json

        return json
