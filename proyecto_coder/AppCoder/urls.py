from django.urls import path
from . import views

urlpatterns=[
    path("", views.buscar_camada, name="home"),
    path("profesores", views.profesores, name="profesores"),
    path("alta_curso",views.curso_formulario,  name="cursos"),
    path("buscar_camada", views.buscar_camada),
    path("buscar", views.buscar),
    path("estudiantes", views.estudiantes, name="estudiantes"),
    path("entregables", views.entregables, name="entregables")
]




