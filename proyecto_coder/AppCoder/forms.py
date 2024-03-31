from django import forms

class Curso_formulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    camada= forms.IntegerField()


class Entregables_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fecha= forms.DateField(input_formats=['%Y-%m-%d'])
    entregado= forms.BooleanField(required=False)

class Estudiante_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.CharField(max_length=30)

class Profesor_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.CharField(max_length=30)
    profesion= forms.CharField(max_length=30)