from django.shortcuts import render,redirect
from django.http import HttpResponse
from application.forms import *
from application.models import *
from authentication.models import *
from application.code_CRUD import *
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


#VISTA HOME
@login_required
def index(request):

    
    avatar = Avatar.objects.filter(usuario = request.user.id).last()
    
    try:
        contexto = {'link1':'home','link2':'negocios','link3':'negocio_3','avatar':avatar.imagen.url,'flag':True}
        return render(request,'application/index.html',contexto)
    except:
        contexto = {'link1':'home','link2':'negocios','link3':'negocio_3'}
        return render(request,'application/index.html',contexto)

#VISTAS NEGOCIO 1
#listar productos
@login_required
def negocio_1_listar(request):
    return listar_productos(
    request= request,
    modelo= Negocio_1,
    titulo= 'Negocio 1', 
    link1= 'home', 
    link2= 'negocio_2_listar', 
    link3= 'negocio_3_listar',
    pagina1='HOME',
    pagina2='NEGOCIO 2',
    pagina3= 'NEGOCIO 3',
    ruta_enviar= 'negocio_1_listar',
    )
#agregar productos
@login_required
def negocio_1_agregar(request):
    return crear_productos(
    request= request,
    titulo= 'Negocio 1', 
    modelo= Negocio_1,
    nombre_vista= 'negocio_1_agregar'
    )    
#actualizar productos
@login_required
def negocio_1_actualizar(request,id_producto):
    return actualizar_producto(
    request= request,
    modelo= Negocio_1,
    nombre_vista= 'negocio_1_listar' ,  
    id_producto= id_producto,
    )
#borrar productos
@login_required
def negocio_1_borrar(request,id_producto):
    return borrar_productos(
    request= request,
    modelo= Negocio_1,
    nombre_vista= 'negocio_1_listar',
    id_producto= id_producto
    )


#VISTAS NEGOCIO 2
#listar productos
@login_required
def negocio_2_listar(request):
    return listar_productos(
    request= request,
    modelo= Negocio_2,
    titulo= 'Negocio 2', 
    link1= 'home', 
    link2= 'negocio_1_listar', 
    link3= 'negocio_3_listar',
    pagina1='HOME',
    pagina2='NEGOCIO 1',
    pagina3= 'NEGOCIO 3',
    ruta_enviar= 'negocio_2_listar'
    )
#agregar productos
@login_required
def negocio_2_agregar(request):
    return crear_productos(
    request= request,
    titulo= 'Negocio 2', 
    modelo= Negocio_2,
    nombre_vista= 'negocio_2_agregar'
    )    
#actualizar productos
@login_required
def negocio_2_actualizar(request,id_producto):
    return actualizar_producto(
    request= request,
    modelo= Negocio_2,
    nombre_vista= 'negocio_2_listar',
    id_producto= id_producto
    )
#borrar productos
@login_required
def negocio_2_borrar(request,id_producto):
    return borrar_productos(
    request= request,
    modelo= Negocio_2,
    nombre_vista= 'negocio_2_listar',
    id_producto= id_producto
    )


#VISTAS NEGOCIO 3
#listar productos
@login_required
def negocio_3_listar(request):
    return listar_productos(
    request= request,
    modelo= Negocio_3,
    titulo= 'Negocio 3', 
    link1= 'home', 
    link2= 'negocio_1_listar', 
    link3= 'negocio_2_listar',
    pagina1='HOME',
    pagina2='NEGOCIO 1',
    pagina3= 'NEGOCIO 2',
    ruta_enviar= 'negocio_3_listar'
    )
#agregar productos
@login_required
def negocio_3_agregar(request):
    return crear_productos(
    request= request,
    titulo= 'Negocio 3', 
    modelo= Negocio_3,
    nombre_vista= 'negocio_3_agregar'
    )    
#actualizar productos
@login_required
def negocio_3_actualizar(request,id_producto):
    return actualizar_producto(
    request= request,
    modelo= Negocio_3,
    nombre_vista= 'negocio_3_listar',
    id_producto= id_producto
    )
#borrar productos
@login_required
def negocio_3_borrar(request,id_producto):
    return borrar_productos(
    request= request,
    modelo= Negocio_3,
    nombre_vista= 'negocio_3_listar',
    id_producto= id_producto
    )
