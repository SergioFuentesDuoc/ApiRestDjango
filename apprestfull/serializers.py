from rest_framework import serializers
from .models import Producto, Usuario


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
