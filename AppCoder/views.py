from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfeForm

# Create your views here.

def curso(request):
    
    curso=Curso(nombre="Curso de Python",comision=123456)
    
    curso.save()
   
    texto=f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)





def inicio(request):
    return render (request, "Appcoder/inicio.html")



def profesores(request):

    

    return render(request, "Appcoder/profesores.html" )

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")

"""
view para formulario a mano!
 def cursoFormulario(request):

    if request.method=="POST":
        nombre=request.POST.get("nombre")
        comision=request.POST.get("comision")
        curso=Curso(nombre=nombre,comision=comision)
        curso.save()
        return render(request, "Appcoder/inicio.html")
    return render(request, "Appcoder/cursoFormulario.html") """


def cursos(request):

    if request.method=="POST":
        miFormulario= CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            nombre=info.get("nombre")
            comision=info.get("comision")
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            return render(request, "Appcoder/inicio.html", {"mensaje": "Curso Creado"})
        else:
            return render(request, "Appcoder/inicio.html", {"mensaje": "Error"})
    
    else:
        miFormulario=CursoFormulario()
        return render(request, "Appcoder/cursos.html", {"formulario":miFormulario})
     

def profeFormulario(request):

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "Profesor Creado"})
        else:
            return render (request, "Appcoder/inicio.html", {"mensaje": "Error"})
    else:
        form= ProfeForm()
    return render(request, "Appcoder/profeFormulario.html", {"formulario":form})


def busquedaComision(request):
    return render(request, "Appcoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comi=request.GET["comision"]
        cursos=Curso.objects.filter(comision=comi)
        if len(cursos)!=0:
            return render(request, "Appcoder/resultadoBusqueda.html", {"cursos":cursos})
        else:
            return render(request, "Appcoder/resultadoBusqueda.html", {"mensaje": "No hay cursos"})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje": "No enviaste datos!"})
    