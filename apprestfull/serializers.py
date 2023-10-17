from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'codigo', 'nombreprod', 'precio', 'cantidad', 'fechaNacimiento', 'rut', 'dv', 'enfermedad', 'fonocontacto', 'categoria', 'editorial', 'raza', 'edad', 'altura', 'hrini', 'hrfin', 'direccion', 'fCreacion')
        read_only_fields = ('fcreacion',)