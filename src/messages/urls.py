from unicodedata import name
from django.urls import path
from messages.views import *

urlpatterns = [
    path('',mensajes,name='messages'),
    path('delete_message/<id_mensaje>',borrar_mensajes,name='delete_message')
]