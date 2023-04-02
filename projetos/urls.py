from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("criando_tarefas", views.criando_projetos),
    path("finalizando_tarefas", views.finalizando_projetos),
]