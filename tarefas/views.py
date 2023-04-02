from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'tarefas/index.html')

def criando_tarefas(request):
    return render(request, 'tarefas/criando_tarefas.html')

def finalizando_tarefas(request):
    return render(request, "tarefas/finalizando_tarefas.html")
