from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("criando_tarefas", views.criando_tarefas),
    path("finalizando_tarefas", views.finalizando_tarefas),
    path("status_ativo", views.status_ativos),
    path("status_finalizado", views.status_finalizados),
]