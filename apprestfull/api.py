from .models import Producto, Usuario, Usuari, Usuario2
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, UsuarioSerializer, UsuariSerializer, Usuario2Serializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class UsuariViewSet(viewsets.ModelViewSet):
    queryset = Usuari.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariSerializer

class Usuario2ViewSet(viewsets.ModelViewSet):
    queryset = Usuario2.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Usuario2Serializer
