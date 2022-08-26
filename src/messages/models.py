from statistics import mode
from django.db import models

# Create your models here.

class Messages(models.Model):
    mensaje = models.CharField(max_length=10000)
    hora_enviado = models.CharField(max_length=20, default='')
    usuario = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.mensaje}'
    
    