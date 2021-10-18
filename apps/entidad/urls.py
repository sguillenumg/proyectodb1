from rest_framework.routers import DefaultRouter
from apps.entidad.views_entidad import EntidadViewSet
router = DefaultRouter(trailing_slash=False)
router.register(r'entidades/?', EntidadViewSet)
url_entidades = router.urls
