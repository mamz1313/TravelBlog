from datetime import datetime
from django.db import models


# Create your models here.

class Post(models.Model):
    id_post = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    img = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Tags(models.Model):
    id_post = models.IntegerField()
    tag = models.CharField(max_length=50)

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    birthday = models.DateField()
    recibir_correos = models.BooleanField()
