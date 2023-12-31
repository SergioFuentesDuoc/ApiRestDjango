from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api   import ProductoViewSet, UsuarioViewSet,UsuariViewSet, Usuario2ViewSet

# Crea un enrutador de DRF
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'usuarios1', UsuariViewSet)
router.register(r'usuarios2', Usuario2ViewSet)

urlpatterns = [
    # Rutas generadas automáticamente por el enrutador de DRF
    path('api/', include(router.urls)),
]

# También puedes agregar rutas personalizadas si es necesario
urlpatterns += [
     path('api/', Usuario2ViewSet.as_view(), name='usuarios2'),
 ]