from django import forms
from .models import *
import bcrypt

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nombre', 'rol']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está en uso.")
        return email
    
    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            usuario.password = hashed_password
        if commit:
            usuario.save()
        return usuario