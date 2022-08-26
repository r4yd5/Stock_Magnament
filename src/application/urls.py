from unicodedata import name
from django.urls import path
from application.views import *


urlpatterns = [
    path('',index,name='home'),
    path('about',sobre_mi,name="about"),

    #listas productos negocios
    path('negocio_1/' ,negocio_1_listar, name='negocio_1_listar'),
    path('negocio_2/' ,negocio_2_listar, name='negocio_2_listar'),
    path('negocio_3/' ,negocio_3_listar, name='negocio_3_listar'),

    #agregar productos negocios
    path('negocio_1/agregar' ,negocio_1_agregar, name='negocio_1_agregar'),
    path('negocio_2/agregar' ,negocio_2_agregar, name='negocio_2_agregar'),
    path('negocio_3/agregar' ,negocio_3_agregar, name='negocio_3_agregar'),

    #actualizar productos negocios
    path('negocio_1/actualizar/<id_producto>' ,negocio_1_actualizar, name='negocio_1_actualizar'),
    path('negocio_2/actualizar/<id_producto>' ,negocio_2_actualizar, name='negocio_2_actualizar'),
    path('negocio_3/actualizar/<id_producto>' ,negocio_3_actualizar, name='negocio_3_actualizar'),

    #borrar productos negocios
    path('negocio_1/borrar/<id_producto>' ,negocio_1_borrar, name='negocio_1_borrar'),
    path('negocio_2/borrar/<id_producto>' ,negocio_2_borrar, name='negocio_2_borrar'),
    path('negocio_3/borrar/<id_producto>' ,negocio_3_borrar, name='negocio_3_borrar')
]