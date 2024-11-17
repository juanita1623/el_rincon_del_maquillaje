from django.shortcuts import render, redirect
from .forms import FormularioPublicacion
from .models import Publicacion

# Create your views here.


def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "inicio.html", {"publicaciones": publicaciones})
    

def crear_publicacion(request):
    if request .method == "GET":
        return render(request, "crear_publicacion.html", { "form": FormularioPublicacion})
    else: 
        form = FormularioPublicacion(request.POST)
        if form.is_valid():
            Publicacion.objects.create (
                titulo = form.cleaned_data['titulo'],
                descripcion = form.cleaned_data['descripcion']
            )
            return  redirect ('inicio')
        
def ver_publicacion(request,publicacion_id):
    publicacion = Publicacion.objects.get(id = publicacion_id)
    return render (request, 'ver_publicacion.html',{"publicacion": publicacion})


