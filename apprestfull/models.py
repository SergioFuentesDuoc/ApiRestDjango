from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto      = models.AutoField( primary_key=True,db_column='id_product')
    codigo          = models.CharField(max_length=10)
    nombreprod      = models.CharField(max_length=20, blank=False, null=False,db_column='desc_prod')
    precio          = models.IntegerField(blank=True, null=True)
    cantidad        = models.IntegerField(blank=True, null=True)
    fechaNacimiento = models.DateField(auto_now_add=True, blank=True, null=True)
    rut             = models.IntegerField(blank=True, null=True)
    dv              = models.CharField(max_length=1)
    enfermedad      = models.CharField(max_length=20)
    fonocontacto    = models.IntegerField(blank=True, null=True)
    categoria       = models.CharField(max_length=20)
    editorial       = models.CharField(max_length=20)
    raza            = models.CharField(max_length=20)
    edad            = models.IntegerField(blank=True, null=True)
    altura          = models.IntegerField(blank=True, null=True)
    hrini           = models.CharField(max_length=5)
    hrfin           = models.CharField(max_length=5)
    direccion       = models.CharField(max_length=20)
    fCreacion       = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.idProducto
    class Meta:
    	db_table = 'producto'
