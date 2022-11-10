"""TravelBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base),
    path('building/', building, name='building'),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('form_suscriptor/', form_suscriptor, name='form_suscriptor'),
    path('form_post/', form_post, name='form_post'),
    path('form_tag/', form_tag, name='form_tag'),
    path('buscar_suscriptor/', buscar_suscriptor, name='buscar_suscriptor'),
    path('buscar_post/', buscar_post, name='buscar_post'),
    path('buscar_tag/', buscar_tag, name='buscar_tag'),
]
