from django import forms


class CursoFormulario(forms.Form):
    #especificar los campos
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()


class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    

    