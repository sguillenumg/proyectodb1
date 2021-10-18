from rest_framework.routers import DefaultRouter
from apps.compra.views_compras import CompraViewSet, DetalleCompraViewSet, EstadoCompraViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'compras/?', CompraViewSet)
router.register(r'detalle-compras/?', DetalleCompraViewSet)
router.register(r'estado-compras/?', EstadoCompraViewSet)

url_compras = router.urls
