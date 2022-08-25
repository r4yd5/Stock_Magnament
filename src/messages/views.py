from django.shortcuts import render,redirect
from django.http import HttpResponse
from messages.forms import *
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

            usuario = request.user.username
            mensaje = data.get('mensaje')

            enviar_mensaje = Messages(usuario= usuario, mensaje=mensaje)

            enviar_mensaje.save()

            return redirect('messages')
        else:
            return render(request, 'messages/mensajes.html',{'form':FormMessages(),'error':'Mensaje no valido'})
            