from django.db import models

# Create your models here.

class Negocio_1(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_individual = models.IntegerField()
    reponer = models.IntegerField()
    observacion = models.CharField(max_length=10000)
    hora_cargado = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'ID: {self.id} - Nombre: {self.nombre_producto}' 


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Negocio 1'


class Negocio_2(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_individual = models.IntegerField()
    reponer = models.IntegerField()
    observacion = models.CharField(max_length=10000)
    hora_cargado = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'ID: {self.id} - Nombre: {self.nombre_producto}' 

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Negocio 2'



class Negocio_3(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_individual = models.IntegerField()
    reponer = models.IntegerField()
    observacion = models.CharField(max_length=10000)
    hora_cargado = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'ID: {self.id} - Nombre: {self.nombre_producto}' 

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Negocio 3'


