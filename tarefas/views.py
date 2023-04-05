from django.shortcuts import render, redirect
import pandas as pd
import os
from datetime import datetime as dt
from django.http import HttpResponse
# Create your views here.
usuario = os.environ['USERPROFILE']
path = os.path.join(usuario, 'Documents', 'github', 'AFRepository')
projetos = pd.read_excel(os.path.join(path, 'projeto.xlsx'), sheet_name="projetos")
projetos = projetos.loc[projetos['status'] == "ativo", 'projetos']
projetos = projetos.values.tolist()

funcionarios = pd.read_excel(os.path.join(path, 'funcionarios.xlsx'), sheet_name="funcionarios")
funcionarios = funcionarios.loc[funcionarios['status'] == "ativo", 'funcionarios']
funcionarios = funcionarios.values.tolist()

tipos_tarefas = pd.read_excel(os.path.join(path, 'tipos_tarefas.xlsx'), sheet_name="tipos_tarefas")
tipos_tarefas = tipos_tarefas.loc[tipos_tarefas['status'] == "ativo", 'tipos_tarefas']
tipos_tarefas = tipos_tarefas.values.tolist()

solicitantes = pd.read_excel(os.path.join(path, 'solicitantes.xlsx'), sheet_name="solicitantes")
solicitantes = solicitantes.loc[solicitantes['status'] == "ativo", 'solicitantes']
solicitantes = solicitantes.values.tolist()

tarefas = pd.read_excel(os.path.join(path, 'tarefas.xlsx'), sheet_name="tarefas")
id_max = tarefas['id'].max()+1
tarefas = tarefas.loc[tarefas['status'] == "ativo"]
tarefas = pd.DataFrame(tarefas)
tarefas = tarefas.to_dict(orient="records")

tarefas_values = []
for tarefa in tarefas:
    tarefa_values = list(tarefa.values())
    tarefas_values.append(tarefa_values)

tarefas_keys = list(tarefas[0].keys())

context = {
    'employees' : funcionarios,
    'projects' : projetos,
    'tasks' : tipos_tarefas,
    'requesters' : solicitantes,
    'df' : tarefas,
    'tarefas_keys' : tarefas_keys,
    'tarefas_values' : tarefas_values
}

def index(request):
    tarefas = pd.read_excel(os.path.join(path, 'tarefas.xlsx'), sheet_name="tarefas")
    tarefas = tarefas.loc[tarefas['status'] == "ativo"]
    tarefas = pd.DataFrame(tarefas)
    tarefas = tarefas.to_dict(orient="records")

    tarefas_values = []
    for tarefa in tarefas:
        tarefa_values = list(tarefa.values())
        tarefas_values.append(tarefa_values)

    tarefas_keys = list(tarefas[0].keys())
    print(tarefas_values)

    context_index = {
        'df': tarefas,
        'tarefas_keys': tarefas_keys,
        'tarefas_values': tarefas_values
    }

    return render(request, 'tarefas/index.html', context_index)

def criando_tarefas(request):
    usuario = os.environ['USERPROFILE']
    path = os.path.join(usuario, 'Documents', 'github', 'AFRepository')
    projetos = pd.read_excel(os.path.join(path, 'projeto.xlsx'), sheet_name="projetos")
    projetos = projetos.loc[projetos['status'] == "ativo", 'projetos']
    projetos = projetos.values.tolist()

    funcionarios = pd.read_excel(os.path.join(path, 'funcionarios.xlsx'), sheet_name="funcionarios")
    funcionarios = funcionarios.loc[funcionarios['status'] == "ativo", 'funcionarios']
    funcionarios = funcionarios.values.tolist()

    tipos_tarefas = pd.read_excel(os.path.join(path, 'tipos_tarefas.xlsx'), sheet_name="tipos_tarefas")
    tipos_tarefas = tipos_tarefas.loc[tipos_tarefas['status'] == "ativo", 'tipos_tarefas']
    tipos_tarefas = tipos_tarefas.values.tolist()

    solicitantes = pd.read_excel(os.path.join(path, 'solicitantes.xlsx'), sheet_name="solicitantes")
    solicitantes = solicitantes.loc[solicitantes['status'] == "ativo", 'solicitantes']
    solicitantes = solicitantes.values.tolist()

    tarefas_at = pd.read_excel(os.path.join(path, 'tarefas.xlsx'), sheet_name="tarefas")
    id_max = tarefas_at['id'].max() + 1
    tarefas = tarefas_at.loc[tarefas_at['status'] == "ativo"]
    tarefas = pd.DataFrame(tarefas)
    tarefas = tarefas.to_dict(orient="records")
    tarefas_at = tarefas_at.to_dict(orient="records")


    context_criando_tarefas = {
        'employees': funcionarios,
        'projects': projetos,
        'tasks': tipos_tarefas,
        'requesters': solicitantes,
        'df': tarefas,
        'df_at': tarefas_at
    }

    if request.method == 'POST':
        # Extrai os valores dos campos do formulário
        employee = request.POST['employee']
        project = request.POST['project']
        task = request.POST['task']
        requester = request.POST['requester']

        # Cria um dicionário com os valores dos campos
        task_data = {
            tarefas_keys[0]: id_max,
            tarefas_keys[1]: task,
            tarefas_keys[2]: employee,
            tarefas_keys[3]: project,
            tarefas_keys[4]: requester,
            tarefas_keys[5]: "ativo",
            tarefas_keys[6]: dt.now().strftime('%Y-%m-%d %H:%M:%S'),
            tarefas_keys[7]: None
        }

        # Faça o que quiser com os valores do dicionário, como salvá-los em um banco de dados

        tarefas_at.append(task_data)

        df = pd.DataFrame(tarefas_at)

        if os.path.exists(os.path.join(path, 'tarefas.xlsx')):
            os.remove(os.path.join(path, 'tarefas.xlsx'))
            df.to_excel(os.path.join(path, 'tarefas.xlsx'),
                             index=False,
                             sheet_name="tarefas"
                             )
        else:
            df.to_excel(os.path.join(path, 'tarefas.xlsx'),
                        index=False,
                        sheet_name="tarefas"
                        )
        return redirect('/')
    return render(request, 'tarefas/criando_tarefas.html', context_criando_tarefas)

def finalizando_tarefas(request):
    tarefas_at = pd.read_excel(os.path.join(path, 'tarefas.xlsx'), sheet_name="tarefas")
    tarefas = tarefas_at.loc[tarefas_at['status'] == "ativo"]
    ids = tarefas['id']
    tarefas = pd.DataFrame(tarefas)
    tarefas = tarefas.to_dict(orient="records")
    tarefas_at = tarefas_at.to_dict(orient="records")
    print(tarefas_at)

    tarefas_values = []
    for tarefa in tarefas:
        print(tarefa)
        tarefa_values = list(tarefa.values())
        tarefas_values.append(tarefa_values)

    tarefas_keys = list(tarefas[0].keys())

    context_finalizando_tarefas = {
        'df': tarefas,
        'tarefas_keys': tarefas_keys,
        'tarefas_values': tarefas_values,
        'ids': ids
    }
    if request.method == 'POST':
        # Extrai os valores dos campos do formulário
        id_select = int(request.POST['ids'])
        for tarefa in tarefas_at:
            if tarefa['id'] == int(id_select):
                tarefa['status'] = "finalizado"
                tarefa['data_finalizacao'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')

        df = pd.DataFrame(tarefas_at)
        if os.path.exists(os.path.join(path, 'tarefas.xlsx')):
            os.remove(os.path.join(path, 'tarefas.xlsx'))
            df.to_excel(os.path.join(path, 'tarefas.xlsx'),
                             index=False,
                             sheet_name="tarefas"
                             )
        else:
            df.to_excel(os.path.join(path, 'tarefas.xlsx'),
                        index=False,
                        sheet_name="tarefas"
                        )
        return redirect('/')

    return render(request, "tarefas/finalizando_tarefas.html", context_finalizando_tarefas)