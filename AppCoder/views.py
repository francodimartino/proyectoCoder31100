from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def curso(request):
    
    curso=Curso(nombre="Curso de Python",comision=123456)
    
    curso.save()
   
    texto=f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)





def inicio(request):
    return render (request, "Appcoder/inicio.html")

def cursos(request):
    curso1=Curso(nombre="Cursito de python",comision=31100)
    curso1.save()
    curso2=Curso(nombre="Cursito de django",comision=31101)
    curso2.save()
    lista=[curso1, curso2]
    return render(request, "Appcoder/cursos.html", {"listita":lista})

def profesores(request):

    

    return render(request, "Appcoder/profesores.html" )

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")
