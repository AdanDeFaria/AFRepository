from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'projetos/index.html')

def criando_projetos(request):
    return render(request, "projetos/criando_projetos.html")

def finalizando_projetos(request):
    return render(request, "projetos/finalizando_projetos.html")