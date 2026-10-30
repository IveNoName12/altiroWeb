from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='mail', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    name = forms.CharField(label='Nombre', max_length=100)
    lastname = forms.CharField(label='Apellido', max_length=100) # Coincide con el HTML
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'lastname', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data