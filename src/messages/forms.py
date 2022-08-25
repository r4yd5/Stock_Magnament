from django import forms

class FormMessages(forms.Form):
    mensaje = forms.CharField(widget=forms.TextInput())
    mensaje.widget.attrs.update({'class': 'input-mensaje','placeholder':'Escribir mensaje...'})