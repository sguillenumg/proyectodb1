from rest_framework.routers import DefaultRouter
from apps.entidad.views_entidad import ClienteViewSet, ProveedorViewSet, EntidadViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'entidades/?', EntidadViewSet)
router.register(r'clientes/?', ClienteViewSet)
router.register(r'proveedores/?', ProveedorViewSet)

url_entidades = router.urls
