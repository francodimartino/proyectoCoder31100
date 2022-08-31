from django.urls import path
from .views import *


urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
    
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profeFormulario/', profeFormulario, name='profeFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    path('leerProfesores/', leerProfesores, name='leerProfesores'),
    path('eliminarProfesor/<id>', eliminarProfesor, name='eliminarProfesor'),
    path('editarProfesor/<id>', editarProfesor, name='editarProfesor'),

    #####
    path('estudiante/list/', EstudianteList.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name='estudiante_borrar'),

   

   



]