from datetime import datetime
from django.db import models


# Create your models here.

class Post(models.Model):
    id_post = models.IntegerField()
    nombre = models.CharField(max_length=50, default='Sin nombre')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=100)
    descripcion = models.TextField()

class Tags(models.Model):
    id_post = models.IntegerField()
    tags = models.CharField(max_length=50)

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    birthday = models.DateTimeField(default=datetime.now)
