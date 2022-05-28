from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class BlogUserForm(UserCreationForm):

    username = forms.CharField(max_length=60, label="Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",
                                widget=forms.PasswordInput
                                )
    password2 = forms.CharField(label="Repita la contraseña",
                                widget=forms.PasswordInput
                                )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("foto_perfil",)

