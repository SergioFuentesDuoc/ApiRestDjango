from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api   import ProductoViewSet, UsuarioViewSet

# Crea un enrutador de DRF
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    # Rutas generadas automáticamente por el enrutador de DRF
    path('api/', include(router.urls)),
]

# También puedes agregar rutas personalizadas si es necesario
# urlpatterns += [
#     path('otra_ruta/', MiVistaPersonalizada.as_view(), name='nombre_ruta_personalizada'),
# ]