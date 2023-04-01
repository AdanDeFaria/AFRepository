from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("criando_tarefas", views.index),
    path("finalizando_tarefas", views.index),
]