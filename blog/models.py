from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo =  models.CharField(max_length=100)
    descripcion = models.TextField()
    autor = models.CharField(default= "Anonimo",max_length=20)
    creacion = models.DateTimeField(auto_now_add=True)