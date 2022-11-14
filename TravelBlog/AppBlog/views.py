from django.shortcuts import render
from .models import *
from .forms import *
from django.forms import ModelForm
# Create your views here.
def base(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'index.html')
def building(request):
    return render(request, 'building.html')
def blog(request):
    return render(request, 'blog.html')

def form_suscriptor(request):
    formulario = CrearSuscriptor()
    
    if request.method == 'POST':
        formulario = CrearSuscriptor(request.POST)
    
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            
            suscriptor = Suscriptor(nombre=formulario_limpio['nombre'],apellido=formulario_limpio['apellido'],email=formulario_limpio['email'], birthday=formulario_limpio['birthday'],recibir_correos=formulario_limpio['recibir_correos'])
            suscriptor.save()
            return render(request,'index.html')
        else:
            formulario = CrearSuscriptor()
        
        
    return render(request, 'form_suscriptor.html',{'formulario':formulario})

def form_post(request):
    formulario = CrearPost()
    
    if request.method == 'POST':
        formulario = CrearPost(request.POST)
    
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            
            post = Post(nombre=formulario_limpio['nombre'],fecha_publicacion=formulario_limpio['fecha_publicacion'],img=formulario_limpio['img'],descripcion=formulario_limpio['descripcion'])
            post.save()
            return render(request,'index.html')
        else:
            formulario = CrearPost()
        
        
    return render(request, 'form_post.html',{'formulario':formulario})


def form_tag(request):
    formulario = Taguear(request.POST or None)
    
    if request.method == 'POST':
        formulario = Taguear(request.POST)
    
        if request.POST and formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            # instance = Tags.id_post.set(Post)
            # tag = Tags(id_tag=formulario_limpio['id_tag'],tag=formulario_limpio['tag'])
            id_tag = formulario_limpio['id_tag']
            tag = formulario_limpio['tag']
            obj = Tags(
                id_tag=id_tag,
                tag = tag
            )
            obj.save()
            # tag.id_post.set(formulario_limpio['id_post'])
            form2 = Taguear(request.POST, instance=obj)
            form2.save(commit=False)
            form2.save_m2m()    
            return render(request,'index.html')
    
    else:
        formulario = Taguear()
        
        
    return render(request, 'form_tag.html',{'formulario':formulario})

def buscar_suscriptor(request):
    
    if request.GET.get('email', False):
        email = request.GET['email']
        suscriptor = Suscriptor.objects.filter(email__icontains=email)
        return render(request, 'buscar_suscriptor.html',{'suscriptores':suscriptor})
    else:
        respuesta = 'No hay datos'
    return render(request,'buscar_suscriptor.html', {'respuesta': respuesta})

def buscar_post(request):
    
    if request.GET.get('id_post', False):
        id_post = request.GET['id_post']
        post = Post.objects.filter(id_post__icontains=id_post)
        # tags = Post.object.filter(Tags__id_tag__icointains=id_post)
        tag = Tags.objects.filter(id_post__id_post__icontains=id_post)
        return render(request, 'buscar_post.html',{'posts':post, 'tags':tag})
        # return render(request, 'buscar_post.html',{'posts':post})
    else:
        respuesta = 'No hay datos'
    return render(request,'buscar_post.html', {'respuesta': respuesta})

def buscar_tag(request):
    
    if request.GET.get('id_tag', False):
        id_tag = request.GET['id_tag']
        tag = Tags.objects.filter(id_tag__exact=id_tag)
        return render(request, 'buscar_tag.html',{'tags':tag})
    else:
        respuesta = 'No hay datos'
    return render(request,'buscar_tag.html', {'respuesta': respuesta})