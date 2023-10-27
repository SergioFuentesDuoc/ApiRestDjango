from .models import Producto, Usuario, Usuari
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, UsuarioSerializer, UsuariSerializer

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
