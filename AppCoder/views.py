from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    


    #    leer profesores

def leerProfesores(request):
    profesores=Profesor.objects.all()
    print(profesores)
    return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})


# eliminar profesor

def eliminarProfesor(request, id):
    profe=Profesor.objects.get(id=id)
    profe.delete()
    profesores=Profesor.objects.all()
    return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})

# editar profesor

def editarProfesor(request, id):
    #traer el profesor
    profe=Profesor.objects.get(id=id)
    if request.method=="POST":
        #el form viene lleno, con los datos a cambiar
        form=ProfeForm(request.POST)
        if form.is_valid():
            #cambio los datos
            info=form.cleaned_data
            profe.nombre=info["nombre"]
            profe.apellido=info["apellido"]
            profe.email=info["email"]
            profe.profesion=info["profesion"]
            #guardo el profe 
            profe.save()
            #vuelvo a la vista del listado para ver el cambio
            profesores=Profesor.objects.all()
            return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})
    else:
        form= ProfeForm(initial={"nombre":profe.nombre, "apellido":profe.apellido, "email":profe.email, "profesion":profe.profesion})
        return render(request, "Appcoder/editarProfesor.html", {"formulario":form, "nombre_profesor":profe.nombre, "id":profe.id})
    
    

###############################################################################################
#vistas basadas en clases para estudiantes

class EstudianteList(ListView):
    model=Estudiante
    template_name="Appcoder/leerEstudiantes.html"

class EstudianteDetalle(DetailView):
    model=Estudiante
    template_name="Appcoder/estudiante_detalle.html"

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')



