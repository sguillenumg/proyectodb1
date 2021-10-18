from rest_framework.routers import DefaultRouter
from apps.venta.views_venta import VentaViewSet, DetalleVentaViewSet, EstadoVentaViewSet, MetodoPagoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'ventas/?', VentaViewSet)
router.register(r'detalle-ventas/?', DetalleVentaViewSet)
router.register(r'estado-ventas/?', EstadoVentaViewSet)
router.register(r'metodos-pago/?', MetodoPagoViewSet)

url_ventas = router.urls
