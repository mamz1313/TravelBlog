from django import forms

class CrearSuscriptor(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    email = forms.EmailField()
    birthday = forms.DateField()
    recibir_correos = forms.BooleanField()

class CrearPost(forms.Form):
    id_post = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    fecha_publicacion = forms.DateField()
    img = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    
class Taguear(forms.Form):
    id_post = forms.IntegerField()
    tag = forms.CharField(max_length=50)