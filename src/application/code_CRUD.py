#funciones para las vistas
from application.models import *
from application.forms import *
from authentication.models import *
from django.shortcuts import render, redirect
import datetime

object_datetime = datetime.datetime.now()
hora = str(object_datetime)
x = slice(19)
hora = hora[x]
        

#listar productos
def listar_productos(request,**kwargs):
    global hora
    avatar = Avatar.objects.filter(usuario = request.user.id).last()
    
    listado_productos = kwargs['modelo'].objects.all()
    contexto = {
        'listado_productos':listado_productos,
        'titulo':kwargs['titulo'],
        'link1':kwargs['link1'],
        'link2':kwargs['link2'],
        'link3':kwargs['link3'],
        'pagina1':kwargs['pagina1'],
        'pagina2':kwargs['pagina2'],
        'pagina3':kwargs['pagina3'],
        'ruta_enviar':kwargs['ruta_enviar']
        }
    try:
        contexto['flag'] = True
        contexto['avatar'] = avatar.imagen.url
    except:
        contexto['flag'] = False
        pass
    form = FormItems()
    if request.GET.get('nombre_producto'):
        listado_productos = listado_productos.filter(nombre_producto__icontains = request.GET.get('nombre_producto'))
        contexto['listado_productos'] = listado_productos
        return render(request,'application/base_negocios.html',contexto)
    else:
        return render(request,'application/base_negocios.html',contexto)
 
#agregar productos
def crear_productos(request,**kwargs):
    global hora
    avatar = Avatar.objects.filter(usuario = request.user.id).last()
    contexto = {
        'titulo':kwargs["titulo"]
        }           
    try:
        contexto['flag'] = True
        contexto['avatar'] = avatar.imagen.url
    except:
        contexto['flag'] = False
        pass

    if request.method == 'GET':
        form = FormItems()
        contexto['form'] = form
        return render(request, 'application/agregar.html', contexto)
    else:
        form = FormItems(request.POST)  
        if form.is_valid():
            data = form.cleaned_data

            producto = data.get('nombre_producto')
            cantidad = data.get('cantidad')
            precio = data.get('precio_individual')
            reponer = data.get('reponer')
            observacion = data.get('observacion')
            hora_cargado = hora
        
            producto_agregado = kwargs['modelo'](
                nombre_producto=producto,
                cantidad=cantidad,
                precio_individual=precio,
                reponer=reponer,
                observacion=observacion,
                hora_cargado = hora_cargado
                )

            producto_agregado.save()

            return redirect(kwargs['nombre_vista'])
        else:
            contexto['form'] = FormItems()
            contexto['error'] = 'Datos no validos'
            return render(request, 'application/agregar.html',contexto)

#actualizar productos
def actualizar_producto(request,id_producto,**kwargs):
    global hora
    producto = kwargs['modelo'].objects.get(id=id_producto)
    
    avatar = Avatar.objects.filter(usuario = request.user.id).last()
    contexto ={
        'nombre_negocio':kwargs['nombre_negocio'],
        'producto':producto
        }
    try:
        contexto['flag'] = True
        contexto['avatar'] = avatar.imagen.url
    except:
        contexto['flag'] = False
        pass

    datos_form = {
        'nombre_producto':producto.nombre_producto,
        'cantidad':producto.cantidad,
        'precio_individual':producto.precio_individual,
        'reponer':producto.reponer,
        'observacion':producto.observacion}

    if request.method == 'GET':
        form = FormItems(initial= datos_form)
        contexto['form'] = form
        return render(request,'application/actualizar.html',contexto)

    else:
        form = FormItems(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            producto.nombre_producto = data.get('nombre_producto')
            producto.cantidad = data.get('cantidad')
            producto.precio_individual = data.get('precio_individual')
            producto.reponer = data.get('reponer')
            producto.observacion = data.get('observacion')
            producto.hora_cargado = hora

            producto.save()

            return redirect(kwargs['nombre_vista'])
        else:
            contexto['form'] = FormItems(initial=datos_form)
            contexto['error'] = 'Datos no validos'
            return render(request, 'application/actualizar.html',contexto)

#borrar productos
def borrar_productos(request, id_producto,**kwargs):
    producto = kwargs['modelo'].objects.get(id=id_producto) 
    avatar = Avatar.objects.filter(usuario = request.user.id).last()
    contexto = {
        'producto':producto,
    }
    try:
        contexto['flag'] = True
        contexto['avatar'] = avatar.imagen.url
    except:
        contexto['flag'] = False
        pass

    if request.method == 'GET':
        return render(request, 'application/borrar.html',contexto)
    else:
        producto.delete()
        return redirect(kwargs['nombre_vista'])