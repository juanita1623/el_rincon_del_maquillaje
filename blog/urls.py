
from django.urls import path
from . import views


urlpatterns = [
    path('crear/', views.crear_publicacion,name= 'crear'),
    path('', views.inicio,name= 'inicio'),
    path('ver/<int:publicacion_id>', views.ver_publicacion , name= 'ver')
]


