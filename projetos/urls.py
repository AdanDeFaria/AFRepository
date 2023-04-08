from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("criando_projetos", views.criando_projetos),
    path("finalizando_projetos", views.finalizando_projetos),
]