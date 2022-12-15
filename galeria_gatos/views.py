from django.shortcuts import render, HttpResponse

# Create your views here.
# a função index está retornando uma página html, a função index é "chamada" no arquivo urls

def index(request):
    return render(request, 'index.html')