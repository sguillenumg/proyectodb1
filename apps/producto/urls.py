from rest_framework.routers import DefaultRouter
from apps.producto.views_producto import ProductoViewSet, InventarioViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'productos/?', ProductoViewSet)
router.register(r'inventarios/?', InventarioViewSet)

url_productos = router.urls
