from rest_framework.routers import DefaultRouter
from .views_seguridad import SeguridadViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'login/?', SeguridadViewSet)

url_seguridad = router.urls
