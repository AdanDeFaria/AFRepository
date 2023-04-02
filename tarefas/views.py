from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
context = {
    'employees' : ["Employee A", "Employee B", "Employee C"],
    'projects' : ["Project X", "Project Y", "Project Z"],
    'tasks' : ["Task 1", "Task 2", "Task 3"],
    'requesters' : ["Requester 1", "Requester 2", "Requester 3"]
}

def index(request):
    return render(request, 'tarefas/index.html')

def criando_tarefas(request):
    return render(request, 'tarefas/criando_tarefas.html', context)

def finalizando_tarefas(request):
    return render(request, "tarefas/finalizando_tarefas.html")
