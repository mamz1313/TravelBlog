from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CrearSuscriptor(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    email = forms.EmailField()
    birthday = forms.DateField()
    recibir_correos = forms.BooleanField()
    
    class Meta:
        model = Suscriptor
        fields = '__all__'

class CrearPost(ModelForm):
    # id_post = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    fecha_publicacion = forms.DateField()
    img = forms.CharField(max_length=100)
    # img = forms.ImageField()
    descripcion = forms.CharField(max_length=100)
    
    class Meta:
        model = Post
        fields = '__all__'
    
class Taguear(ModelForm):
    id_tag = forms.IntegerField(label='id_tag')
    # id_post = forms.ModelChoiceField(queryset=Post.objects.all(), empty_label='Seleccione un id post')
    id_post = forms.ModelMultipleChoiceField(queryset=Post.objects.all().order_by('nombre'),label='id_post', widget=forms.CheckboxSelectMultiple)
    tag = forms.CharField(max_length=50)
    
    class Meta:
        model = Tags
        fields = '__all__'
        

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
class UserEditForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}
        
