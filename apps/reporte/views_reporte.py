from django.shortcuts import render
from base.viewset_base import ViewsetBase
from rest_framework.response import Response
from django.db import transaction
from apps.venta.serializer import VentaSerializer
from apps.venta.models import Venta
from apps.sucursal.models import Sucursal
from rest_framework.decorators import action

class ReporteViewSet(ViewsetBase):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    modelo = Venta

    @action(methods=['get'], detail=False, url_path='1')
    def reporte1(self, request):
        qry = """
            SELECT * FROM (
                SELECT
                    ROWNUM ROW_ID,
                    MOV.*
                FROM (
                    SELECT
                        SUC.ID,
                        SUC.DIRECCION,
                        PROD.NOMBRE,
                        SUM(DET.CANTIDAD) TOTAL
                    FROM VENTAS VEN
                    JOIN VENTA_DETALLES DET ON DET.VENTA_ID = VEN.ID
                    JOIN PRODUCTOS PROD ON PROD.ID = DET.PRODUCTO_ID
                    JOIN SUCURSALES SUC ON SUC.ID = VEN.SUCURSAL_ID
                    WHERE SUC.ID = {}
                    GROUP BY
                        SUC.ID,
                        SUC.DIRECCION,
                        PROD.NOMBRE
                    ORDER BY
                        4 DESC
                ) MOV
            ) A
            WHERE
                ROW_ID BETWEEN 0 AND 5
        """

        with connection.cursor() as cursor:
            resultado = []
            
            sucursales = list(Sucursal.objects.all())
            for suc in sucursales:
                cursor.execute(qry.format(suc.id))
                resultado.extend(self.dictfetchall(cursor))

            return Response(resultado, 200)

    @action(methods=['get'], detail=False, url_path='2')
    def reporte2(self, request):
        qry = """
            SELECT * FROM (
                SELECT
                    ROWNUM ROW_ID,
                    MOV.*
                FROM (
                    SELECT
                        SUC.ID,
                        SUC.DIRECCION,
                        ENT.DPI,
                        ENT.NOMBRE,
                        ENT.APELLIDO,
                        SUM(VEN.TOTAL) TOTAL
                    FROM VENTAS VEN
                    JOIN CLIENTES CLI ON CLI.ID = VEN.CLIENTE_ID
                    JOIN ENTIDADES ENT ON ENT.ID = CLI.ENTIDAD_ID
                    JOIN SUCURSALES SUC ON SUC.ID = VEN.SUCURSAL_ID
                    WHERE SUC.ID = {}
                    GROUP BY
                        SUC.ID,
                        SUC.DIRECCION,
                        ENT.DPI,
                        ENT.NOMBRE,
                        ENT.APELLIDO
                    ORDER BY
                        6 DESC
                ) MOV
                ) A
                WHERE
                ROW_ID BETWEEN 0 AND 10
        """

        with connection.cursor() as cursor:
            resultado = []

            sucursales = list(Sucursal.objects.all())
            for suc in sucursales:
                cursor.execute(qry.format(suc.id))
                resultado.extend(self.dictfetchall(cursor))

            return Response(resultado, 200)
    
    @action(methods=['get'], detail=False, url_path='3')
    def reporte3(self, request):
        qry = """
            SELECT * FROM (
                SELECT
                    ROWNUM ROW_ID,
                    MOV.*
                FROM (
                    SELECT
                        SUC.ID,
                        SUC.DIRECCION,
                        PROD.NOMBRE,
                        SUM(DET.CANTIDAD) TOTAL
                    FROM VENTAS VEN
                    JOIN VENTA_DETALLES DET ON DET.VENTA_ID = VEN.ID
                    JOIN PRODUCTOS PROD ON PROD.ID = DET.PRODUCTO_ID
                    JOIN SUCURSALES SUC ON SUC.ID = VEN.SUCURSAL_ID
                    WHERE SUC.ID = {}
                    GROUP BY
                        SUC.ID,
                        SUC.DIRECCION,
                        PROD.NOMBRE
                    ORDER BY
                        4 ASC
                ) MOV
            ) A
            WHERE
                ROW_ID BETWEEN 0 AND 5
        """

        with connection.cursor() as cursor:
            resultado = []

            sucursales = list(Sucursal.objects.all())
            for suc in sucursales:
                cursor.execute(qry.format(suc.id))
                resultado.extend(self.dictfetchall(cursor))

            return Response(resultado, 200)

    @classmethod
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
