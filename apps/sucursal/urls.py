from rest_framework.routers import DefaultRouter
from apps.sucursal.views_sucursal import SucursalViewSet, EmpleadoViewSet, TurnoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'sucursales/?', SucursalViewSet)
router.register(r'empleados/?', EmpleadoViewSet)
router.register(r'turnos/?', TurnoViewSet)

url_sucursales = router.urls
