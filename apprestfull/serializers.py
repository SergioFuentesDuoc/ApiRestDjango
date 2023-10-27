from rest_framework import serializers
from .models import Producto, Usuario, Usuari, Usuario2


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'codigo', 'nombreprod', 'precio', 'cantidad', 'fechaNacimiento', 'rut', 'dv', 'enfermedad', 'fonocontacto', 'categoria', 'editorial', 'raza', 'edad', 'altura', 'hrini', 'hrfin', 'direccion', 'fCreacion')
        read_only_fields = ('fCreacion',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('fCreacionu',)

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = '__all__'
        read_only_fields = ('fCreacionui',)

class Usuario2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario2
        fields = '__all__'
        read_only_fields = ('fCreacionu2',)
