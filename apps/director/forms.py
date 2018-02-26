from django import forms
from django.contrib.auth.models import User
from apps.director.models import Perfil, Alumnos

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        'first_name','last_name','email','username',
        ]


class PerfilUserForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
        'numDocumento','area','perfil','imgUser',
        ]

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = [
        'nombres','apellidos','escuela','numDocumento','fechaNacimiento',
        'email','activo','imgAlumno',
        ]
