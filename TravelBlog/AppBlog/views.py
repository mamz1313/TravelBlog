from django.shortcuts import render
from .models import *
# from .forms import *
# Create your views here.
def base(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'index.html')
def building(request):
    return render(request, 'building.html')
def blog(request):
    return render(request, 'blog.html')
