from django.db import models

# Create your models here.

class Messages(models.Model):
    mensaje = models.CharField(max_length=10000)
    usuario = models.CharField(max_length=10000)