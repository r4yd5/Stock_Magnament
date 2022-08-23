from re import template
from unicodedata import name
from django.urls import path
from authentication.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', iniciar_sesion, name='login'),
    path('signup/', registrarse, name='signup'),
    path('logout/', LogoutView.as_view(), name= 'logout'),
    path('profile/', perfil, name='profile'),
    path('profile/edit_profile/', editar_perfil, name='edit_profile'),
    path('profile/change_password/', cambiar_contrasenia, name='change_password'),
    path('profile/change_avatar/',cambiar_avatar,name='change_avatar'),
    path('profile/delete_avatar/',borrar_avatar,name='delete_avatar')
]