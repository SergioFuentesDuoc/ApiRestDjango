from rest_framework import serializers
from .models import Producto, Usuario, Usuari, Usuario2


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'codigo', 'nombreprod', 'precio', 'cantidad', 'fechaNacimiento', 'rut', 'dv', 'enfermedad', 'fonocontacto', 'categoria', 'editorial', 'raza', 'edad', 'altura', 'hrini', 'hrfin', 'direccion', 'fCreacion')
        read_only_fields = ('fcreacion',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_email', 'first_name', 'last_name', 'clave', 'grupo_usu', 'estado_usu', 'fCreacionu')
        read_only_fields = ('fCreacionu',)

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = ('id_emaili', 'codigoi','first_namei', 'last_namei','clavei', 'grupo_usui', , 'estado_usui','fCreacionui')
        read_only_fields = ('fCreacionui',)

class Usuario2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario2
        fields = ('id_correo', 'id_email2', 'codigo2','first_name2', 'last_name2','clave2', 'grupo_usu2', 'fCreacionu2')
        read_only_fields = ('fCreacionu2',)
