from django.urls import path, include
from rest_framework import routers
from .api   import ProductoViewSet, UsuarioViewSet

router = routers.DefaultRouter()

#router.register('api/productos', ProductoViewSet, 'productos')
#router.register('api/usuarios', UsuarioViewSet, 'usuarios')

#urlpatterns = router.urls

router.register('api/productos', ProductoViewSet, 'productos',basename="productos")
router.register('api/usuarios', UsuarioViewSet, 'usuarios',basename="usuarios")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]