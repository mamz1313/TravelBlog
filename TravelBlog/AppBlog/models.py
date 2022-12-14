from datetime import datetime
from django.db import models
from django.forms import ModelForm


# Create your models here.

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    img = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='static/assets/img'
    descripcion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id_post']
    
    def __str__(self):
        return self.nombre

class Tags(models.Model):
    id_tag = models.IntegerField(primary_key=True)
    id_post = models.ManyToManyField(Post, default=1, related_name='post_tags')
    tag = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['id_tag']
        
    def __str__(self):
        return self.tag

class Suscriptor(models.Model):
    id_suscriptor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    birthday = models.DateField()
    recibir_correos = models.BooleanField()

    def __str__(self):
        return self.nombre