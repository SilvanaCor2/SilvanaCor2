from rest_framework import routers
from .api import LibrosViewSet

router = routers.DefaultRouter()

router.register('api/libros', LibrosViewSet,'libros')

urlpatterns = router.urls