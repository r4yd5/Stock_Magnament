from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from final_project import settings
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    sitio_link = models.CharField(max_length=155, blank=True)
    descripcion = RichTextField(default="-")

    

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)


    def borrar(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.imagen.name))
        super(Avatar,self).delete(*args,**kwargs)


    
