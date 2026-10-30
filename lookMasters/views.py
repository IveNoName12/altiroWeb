from django.shortcuts import render

# Create your views here.
def masters(request):
    return render(request, 'masters/maestros.html')