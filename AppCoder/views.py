from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfeForm, UserRegisterForm, UserEditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




#imports para login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def curso(request):
    
    curso=Curso(nombre="Curso de Python",comision=123456)
    
    curso.save()
   
    texto=f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)




@login_required
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

@login_required
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

class EstudianteList(LoginRequiredMixin, ListView):
    model=Estudiante
    template_name="Appcoder/leerEstudiantes.html"

class EstudianteDetalle(LoginRequiredMixin, DetailView):
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



#----- Login, logout y registro de usuarios


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppCoder/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppCoder/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form':form})


def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            #podriamos fijarnos que no exista un user en la bd con ese nombre

            form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, 'AppCoder/register.html', {'form':form})

        
@login_required        
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f"Perfil de {usuario} editado"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'AppCoder/editarPerfil.html', {'form':form, 'usuario':usuario})
