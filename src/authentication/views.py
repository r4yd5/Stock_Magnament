from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.forms import *
from django.contrib.auth import authenticate, login
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def iniciar_sesion(request):

    if request.user.is_authenticated == False:
        if request.method == 'GET':
            form = CustomUserAuthenticationForm()
            return render(request, 'authentication/login.html',{'form': form})
        else:
            form = CustomUserAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                data = form.cleaned_data

                username = data.get('username')
                password = data.get('password')


                user = authenticate(username= username, password= password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                return render(request, 'authentication/login.html', {'error':'Usuario/Contraseña incorrectos','form':CustomUserAuthenticationForm()})
    else:
        return redirect('home')


def registrarse(request):
    if request.user.is_authenticated == False:
        if request.method == 'GET':
            form = CustomUserCreationForm()
            return render(request, 'authentication/signup.html',{'form':form})

        else:
            form = CustomUserCreationForm(request.POST)
            try:
                form.save()
                return redirect('login')
            except:
                return render(request, 'authentication/signup.html',{'form':form})
    else:
        return redirect('home')


@login_required 
def perfil(request):
    try:
        avatar = Avatar.objects.filter(usuario= request.user.id).last()
        return render(request, 'authentication/profile.html', {'avatar':avatar.imagen.url,'flag':True})
    except:
        return render(request, 'authentication/profile.html')


@login_required        
def editar_perfil(request):

    datos_formulario = {
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'sitio_link':request.user.sitio_link,
        'descripcion':request.user.descripcion
    }

    if request.method == 'GET':
        form = CustomUserEditingForm(initial= datos_formulario)
        return render(request, 'authentication/edit_profile.html',{'form':form})
    else:
        form = CustomUserEditingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            usuario.email = data.get('email')
            usuario.sitio_link = data.get('sitio_link')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')
            usuario.descripcion = data.get('descripcion')

            usuario.save()
            
            return redirect('profile')
        else:
            return render(request, 'authentication/edit_profile.html',{'form':form,'error':'Datos no validos'})

            
@login_required
def cambiar_contrasenia(request):
    if request.method == 'GET':
        form = ChangePassword()
        return render(request, 'authentication/change_password.html',{'form':form})
    else:
        form = ChangePassword(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            usuario.password1 = data.get('password1')
            usuario.password2 = data.get('password2')

            usuario.save()

            return redirect('profile')
           
        else:
            return render(request, 'authentication/change_password.html',{'form':form,'error':'Datos no validos'})


@login_required
def cambiar_avatar(request):
    if request.method == 'GET':
        form = AvatarForm()
        return render(request, 'authentication/change_avatar.html',{'form':form})
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            
            #me traigo el username del usuario logueado
            usuario_avatar = User.objects.filter(username=request.user.username).first()
            
            #fitlro el usuario logueado y borro su viejo avatar
            usuario_filtrado = Avatar.objects.filter(usuario=request.user.id)
            for avatar_viejo in usuario_filtrado:
                avatar_viejo.borrar()
            
            #instancio un objeto de la clase del modelo avatar con el usuario y la nueva imagen
            avatar = Avatar(usuario= usuario_avatar, imagen=data['image'])
            avatar.save() #guardo la nueva imagen

            return redirect('profile')

        else:
            return render(request, 'authentication/change_avatar.html', {'error':'Archivo no valido','form':AvatarForm()})


@login_required
def borrar_avatar(request):
    usuario_filtrado = Avatar.objects.filter(usuario=request.user.id)
    for avatar_viejo in usuario_filtrado:
        avatar_viejo.borrar()
    return redirect('profile')
            
        
