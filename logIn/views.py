from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'logIn/login.html')

def register(request):
    return render(request, 'logIn/register.html')