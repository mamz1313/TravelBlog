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
    path('login2/', login2, name='login2'),
    path('nosotros/', nosotros, name='nosotros'),
    path('blog/', blog, name='blog'),
    path('form_suscriptor/', form_suscriptor, name='form_suscriptor'),
    path('post_form/', post_form, name='post_form'),
    path('form_tag/', form_tag, name='form_tag'),
    path('buscar_suscriptor/', buscar_suscriptor, name='buscar_suscriptor'),
    path('buscar_post/', buscar_post, name='buscar_post'),
    path('buscar_tag/', buscar_tag, name='buscar_tag'),
    
    # Post
    path('list_post/', PostListView.as_view(), name='Post_ListView'),
    path('detail_post/<pk>', PostDetailView.as_view(), name='Post_DetailView'),
    path('delete_post/<pk>', PostDeleteView.as_view(), name='Post_DeleteView'),
    path('update_post/<pk>', PostUpdateView.as_view(), name='Post_UpdateView'),
    path('form_post/', PostCreateView.as_view(), name='Post_CreateView'),
    
    # Suscriptor
    path('list_suscriptor/', SuscriptorListView.as_view(), name='Suscriptor_ListView'),
    path('detail_suscriptor/<pk>', SuscriptorDetailView.as_view(), name='Suscriptor_DetailView'),
    path('delete_suscriptor/<pk>', SuscriptorDeleteView.as_view(), name='Suscriptor_DeleteView'),
    path('update_suscriptor/<pk>', SuscriptorUpdateView.as_view(), name='Suscriptor_UpdateView'),
    path('form_suscriptor/', SuscriptorCreateView.as_view(), name='Suscriptor_CreateView'),

    # Tags
    path('list_tags/', TagsListView.as_view(), name='Tags_ListView'),
    path('detail_tags/<pk>', TagsDetailView.as_view(), name='Tags_DetailView'),
    path('delete_tags/<pk>', TagsDeleteView.as_view(), name='Tags_DeleteView'),
    path('update_tags/<pk>', TagsUpdateView.as_view(), name='Tags_UpdateView'),
    path('form_tags/', TagsCreateView.as_view(), name='Tags_CreateView'),
    
    
    #SignUp    
    path('signup/',SignUpView.as_view(), name="Sign Up"),
    
    #Login/Logout
    path('login/',AdminLoginView.as_view(), name="Login"),    
    path('logout/',AdminLogoutView.as_view(), name="Logout"),
]
