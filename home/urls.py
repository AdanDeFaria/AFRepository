from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("projetos/", views.projetos),
    path("tarefas/", views.tarefas),
    path("tarefas/criando", views.criando_tarefas),
    path("tarefas/finalizando", views.finalizando_tarefas),
    path("projetos/criando", views.criando_projetos),
    path("projetos/finalizando", views.finalizando_projetos),
    path("tarefas/ativo", views.status_ativos_tarefas),
    path("tarefas/finalizado", views.status_finalizados_tarefas),
]