from django.urls import path
from messages.views import *

urlpatterns = [
    path('',mensajes,name='messages')
]