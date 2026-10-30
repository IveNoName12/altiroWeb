from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

from logIn.forms import LoginForm, RegisterForm

# Cambiamos el nombre de la vista para que no colisione con la función login de Django
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user_obj = User.objects.get(email=email)
                # Autenticamos usando el username real que guardamos en la BD
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/')  # Redirige a la página de inicio después del login exitoso
                else:
                    return HttpResponse("Cuenta desactivada")
    else:
        form = LoginForm()
    return render(request, 'logIn/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        # AQUÍ ESTABA EL ERROR: Debes usar tu RegisterForm, no UserCreationForm pelado
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Guardamos el usuario de forma segura
            user = form.save(commit=False)
            # Si el username es obligatorio en Django y usas el email como username:
            user.username = form.cleaned_data['email'] 
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/login/')  
        else:
            print("Errores en el registro:", form.errors) # Esto te imprimirá en consola si algo falla
    else:
        form = RegisterForm()
    return render(request, 'logIn/register.html', {'form': form})