from django.shortcuts import render,redirect
from messages.forms import *
from django.contrib.messages import error
from messages.models import Messages
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

@login_required
def mensajes(request):
    mensj = Messages.objects.all()
    if request.method == 'GET':
        form = FormMessages()
        return render(request, 'messages/mensajes.html', {'mensj':mensj,'form':form})
    else:
        form = FormMessages(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            object_datetime = datetime.datetime.now()
            hora = str(object_datetime)
            x = slice(19)
            hora = hora[x]


            usuario = request.user.username
            mensaje = data.get('mensaje')
            hora_enviado = hora
            enviar_mensaje = Messages(usuario= usuario, mensaje=mensaje, hora_enviado= hora_enviado)

            enviar_mensaje.save()
            
            return redirect('messages')
        else:
            return render(request, 'messages/mensajes.html',{'form':FormMessages(),'error':'Mensaje no valido'})

@login_required       
def borrar_mensajes(request,id_mensaje):
    mensaje_a_borrar = Messages.objects.get(id=id_mensaje)
    if request.method == 'GET':
        return render(request, 'messages/borrar_mensaje.html',{'msj':mensaje_a_borrar})
    else:
        if mensaje_a_borrar.usuario == request.user.username or request.user.is_staff == 1:
            mensaje_a_borrar.delete()
            return redirect('messages')
        else:
            error(request, 'NO TIENES PERMISO PARA BORRAR ESTE MENSAJE')
            return redirect('messages')