from django.shortcuts import render
import pandas as pd
import os
from django.http import HttpResponse
# Create your views here.
usuario = os.environ['USERPROFILE']
print(usuario)
path = os.path.join(usuario, 'Documents', 'github', 'AFRepository', 'projeto.xlsx')
projetos = pd.read_excel(path, sheet_name="projetos")
projetos = projetos.loc[projetos['status'] == "ativo", 'projetos']
projetos = projetos.values.tolist()

funcionarios = pd.read_excel(path, sheet_name="funcionarios")
funcionarios = funcionarios.loc[funcionarios['status'] == "ativo", 'funcionarios']
funcionarios = funcionarios.values.tolist()

funcionarios = pd.read_excel(path, sheet_name="funcionarios")
funcionarios = funcionarios.loc[funcionarios['status'] == "ativo", 'funcionarios']
funcionarios = funcionarios.values.tolist()
print(funcionarios)

context = {
    'employees' : funcionarios,
    'projects' : projetos,
    'tasks' : ["Task 1", "Task 2", "Task 3"],
    'requesters' : ["Requester 1", "Requester 2", "Requester 3"]
}

def index(request):
    return render(request, 'tarefas/index.html')

def criando_tarefas(request):
    return render(request, 'tarefas/criando_tarefas.html', context)

def finalizando_tarefas(request):
    return render(request, "tarefas/finalizando_tarefas.html", context)
