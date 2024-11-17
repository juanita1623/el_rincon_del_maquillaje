from django import forms

class FormularioPublicacion(forms.Form):
    titulo = forms.CharField(label= " Titulo publicacion ", max_length= 100, required=True)
    descripcion = forms.CharField(label= "Descripcion de la publicacion", widget= forms.Textarea,required=False)