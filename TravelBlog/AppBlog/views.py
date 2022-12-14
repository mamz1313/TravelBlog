from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Redirección
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def index(request):
    return render(request, 'index.html')
def login2(request):
    return render(request, 'login2.html')
def nosotros(request):
    return render(request, 'nosotros.html')
@login_required
def building(request):
    return render(request, 'building.html')
@login_required
def blog(request):
    return render(request, 'blog.html')

@login_required
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

@login_required
def post_form(request):
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
        
        
    return render(request, 'post_form.html',{'formulario':formulario})

@login_required
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

@login_required
def buscar_suscriptor(request):
    
    if request.GET.get('email', False):
        email = request.GET['email']
        suscriptor = Suscriptor.objects.filter(email__icontains=email)
        return render(request, 'buscar_suscriptor.html',{'suscriptores':suscriptor})
    else:
        respuesta = 'No hay datos'
    return render(request,'buscar_suscriptor.html', {'respuesta': respuesta})

@login_required
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

@login_required
def buscar_tag(request):
    
    if request.GET.get('id_tag', False):
        id_tag = request.GET['id_tag']
        tag = Tags.objects.filter(id_tag__exact=id_tag)
        return render(request, 'buscar_tag.html',{'tags':tag})
    else:
        respuesta = 'No hay datos'
    return render(request,'buscar_tag.html', {'respuesta': respuesta})
    
# -------------------------------Suscriptor Class-------------------------------
class SuscriptorListView(LoginRequiredMixin,ListView):
    model = Suscriptor
    template_name = 'AppBlog/suscriptor_list.html'
    
class SuscriptorDetailView(LoginRequiredMixin,DetailView):
    model = Suscriptor
    template_name = 'AppBlog/suscriptor_detail.html'

class SuscriptorDeleteView(LoginRequiredMixin,DeleteView):
    model = Suscriptor
    success_url = '/list_suscriptor'
    
class SuscriptorUpdateView(LoginRequiredMixin,UpdateView):
    model = Suscriptor
    success_url = '/list_suscriptor'
    fields = ['nombre','apellido','email','birthday','recibir_correos']

class SuscriptorCreateView(LoginRequiredMixin,CreateView):
    model = Suscriptor
    success_url = '/list_suscriptor'
    fields = ['nombre','apellido','email','birthday','recibir_correos']


# -------------------------------Post Class-------------------------------
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'AppBlog/post_list.html'
    
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/list_post'
    
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = '/list_post'
    fields = ['nombre','fecha_publicacion','img','descripcion']

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    success_url = '/list_post'
    fields = ['nombre','fecha_publicacion','img','descripcion']
    
# -------------------------------Tag Class-------------------------------
class TagsListView(LoginRequiredMixin,ListView):
    model = Tags
    template_name = 'AppBlog/tags_list.html'
    
class TagsDetailView(LoginRequiredMixin,DetailView):
    model = Tags
    template_name = 'AppBlog/tags_detail.html'
    contex_object_name = 'post'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        post_tags = Tags.objects.all()
        context['related'] = Post.objects.filter(id_post__in=post_tags)[:3]
        return context

class TagsDeleteView(LoginRequiredMixin,DeleteView):
    model = Tags
    success_url = '/list_tags'
    
class TagsUpdateView(LoginRequiredMixin,UpdateView):
    model = Tags
    success_url = '/list_tags'
    fields = ['id_tag','id_post','tag']

class TagsCreateView(LoginRequiredMixin,CreateView):
    model = Tags
    success_url = '/list_tags'
    fields = ['id_tag','id_post','tag']
    

#USER
class SignUpView(CreateView):
    
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'registro.html'
    class Meta:
        pass

class AdminLoginView(LoginView):
    template_name = 'login.html'


class AdminLogoutView(LogoutView):
    template_name = 'logout.html'