from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.models import User
from ckeditor.widgets import CKEditorWidget




class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder':'Contraseña'}))

    class Meta:
        fields = ['username','password']
        


class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Usuario'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'fadeIn third', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Confirmar contraseña'}))

  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
        


class CustomUserEditingForm(UserCreationForm):
    first_name = forms.CharField(label= 'NOMBRE', max_length=50, widget=forms.TextInput(attrs={'class': 'fadeIn third', 'placeholder': 'Nombre'}), required=False)
    last_name = forms.CharField(label= 'APELLIDO', max_length=50, widget=forms.TextInput(attrs={'class': 'fadeIn third', 'placeholder': 'Apellido'}), required=False)
    sitio_link = forms.CharField(label= 'SITIO WEB', max_length=50, widget=forms.TextInput(attrs={'class': 'fadeIn third', 'placeholder': 'Link'}), required=False)
    email = forms.EmailField(label= 'EMAIL', widget=forms.TextInput(attrs={'class': 'fadeIn third', 'placeholder': 'Email'}), required=False)
    descripcion = forms.CharField(label= 'DESCRIPCION', widget=CKEditorWidget(),required=False)
    password1 = None
    password2 = None
    

    class Meta:
        model = User
        fields = ['email','first_name','last_name', 'sitio_link']
        help_texts = {k:'' for k in fields}

class ChangePassword(UserCreationForm):
    password1 = forms.CharField(label='NUEVA CONTRESEÑA' ,widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='CONFIRMAR CONTRESEÑA' ,widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ['password1', 'password2',]
        help_texts = {k:'' for k in fields}


class AvatarForm(forms.Form):
    image = forms.ImageField()
    image.widget.attrs.update({'class': 'form-img','value':'a'})

    