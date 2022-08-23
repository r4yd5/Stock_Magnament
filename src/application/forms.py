from django.forms import Form, IntegerField, CharField
from django import forms


class FormItems(Form):
    nombre_producto = CharField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}))
    cantidad = IntegerField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}))
    precio_individual = IntegerField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}))
    reponer = IntegerField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}))
    observacion = CharField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}), required=None)