from django.shortcuts import render
from AppCoder.models import Curso, Entregables, Estudiante, Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Entregables_formulario, Estudiante_formulario, Profesor_formulario

# Create your views here.
def curso_formulario(request):
    if request.method == "POST":
        mi_formulario=Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso=Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario_curso.html")

    return render(request, "formulario_curso.html")
def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar_camada(request):
    return render(request, "buscar_camada.html")

def alta_curso(request,nombre):
    curso=Curso(nombre=nombre, camada=123445)
    curso.save()
    texto=f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def inicio(request):
    return render(request , "padre.html")




def buscar(request):
    if request.GET["camada"]:
        nombre=request.GET["camada"]
        cursos=Curso.objects.filter(camada__icontains=nombre)
        return render(request, "resultado_busqueda_camada.html",{"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

def entregables(request):
    if request.method == "POST":
        mi_formulario=Entregables_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            entregable=Entregables(nombre=datos["nombre"], fecha=datos["fecha"], entregado=datos["entregado"])

            entregable.save()
            return render(request, "formulario_entregable.html")

    return render(request, "formulario_entregable.html")    

def estudiantes(request):
    if request.method == "POST":
        mi_formulario=Estudiante_formulario(request.POST)

        if mi_formulario.is_valid():

            datos=mi_formulario.cleaned_data
            estudiante=Estudiante(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"])
            estudiante.save()
            return render(request, "formulario_estudiantes.html")

    return render(request, "formulario_estudiantes.html")    

def profesores(request):
    if request.method == "POST":
        mi_formulario=Profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesor=Profesor(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"], profesion=datos["profesion"])
            profesor.save()
            return render(request, "formulario_profesor.html")

    return render(request, "formulario_profesor.html")   