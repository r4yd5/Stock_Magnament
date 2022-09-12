from django.forms import Form, IntegerField, CharField
from django import forms


class FormItems(Form):
    nombre_producto = CharField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}))
    cantidad = IntegerField()
    precio_individual = IntegerField()
    reponer = IntegerField()
    observacion = CharField(widget= forms.TextInput(attrs={'class': 'formularios-actualizar'}), required=None)
    cantidad.widget.attrs.update({'class': 'formularios-actualizar'})
    precio_individual.widget.attrs.update({'class': 'formularios-actualizar'})
    reponer.widget.attrs.update({'class': 'formularios-actualizar'})
    
