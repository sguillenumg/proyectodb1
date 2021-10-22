from rest_framework.routers import DefaultRouter
from .views_reporte import ReporteViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'reportes/?', ReporteViewSet)

url_reportes = router.urls
