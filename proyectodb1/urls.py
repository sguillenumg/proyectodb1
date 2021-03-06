from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.entidad.urls import url_entidades
from apps.sucursal.urls import url_sucursales
from apps.producto.urls import url_productos
from apps.venta.urls import url_ventas
from apps.compra.urls import url_compras
from apps.seguridad.urls import url_seguridad
from apps.reporte.urls import url_reportes

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns += url_entidades
urlpatterns += url_sucursales
urlpatterns += url_productos
urlpatterns += url_ventas
urlpatterns += url_compras
urlpatterns += url_seguridad
urlpatterns += url_reportes

urlpatterns += [
    path('admin/', admin.site.urls),
]
