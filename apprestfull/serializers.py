from rest_framework import serializers
from .models import Producto, Usuario, Usuari


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'codigo', 'nombreprod', 'precio', 'cantidad', 'fechaNacimiento', 'rut', 'dv', 'enfermedad', 'fonocontacto', 'categoria', 'editorial', 'raza', 'edad', 'altura', 'hrini', 'hrfin', 'direccion', 'fCreacion')
        read_only_fields = ('fcreacion',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_email', 'first_name', 'last_nam','clave', 'grupo_usu', 'fCreacionu')
        read_only_fields = ('fcreacionu',)

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = ('id_emaili', 'codigoi','first_namei', 'last_nami','clavei', 'grupo_usui', 'fCreacionui')
        read_only_fields = ('fcreacionui',)
