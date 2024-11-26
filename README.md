# el_rincon_del_maquillaje

# Blog de Maquillaje 💄✨

Este es un blog funcional desarrollado en Django, diseñado para compartir publicaciones relacionadas con el mundo del maquillaje.

## 📋 Funcionalidades del Blog

1. **Página de inicio**  
   Lista todas las publicaciones, mostrando:  
   - Título  
   - Extracto del contenido  
   - Fecha de publicación  

2. **Vista detallada**  
   Permite visualizar el contenido completo de una publicación al hacer clic en su título.  

3. **Formulario de creación**  
   Agrega nuevas publicaciones desde la web, sin necesidad de acceder al panel de administración.

## 🛠️  Publicación
El modelo incluye los siguientes campos:  
- `título`: Texto breve y descriptivo.  
- `contenido`: Detalle completo de la publicación.  
- `autor`: Nombre del autor, con un valor predeterminado de "Anónimo".  
- `fecha_de_publicación`: Fecha y hora de creación.  

## 🚀 Ejecución

### **Requisitos previos**
- Python 3.x  
- pip (gestor de paquetes de Python)  
- Django 4.x  

### **Instrucciones de instalación**
 ```bash
   git clone https://github.com/juanita1623/el_rincon_del_maquillaje.git
   cd blog-maquillaje

### 🚀 Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto:
 
🛠️ Crea y activa un entorno virtual  

   python -m venv venv
   source venv/bin/activate  

📦 Asegúrate de instalar todos los paquetes necesarios con el siguiente comando:

    pip install -r requirements.txt

🚀 Inicia el proyecto localmente con:
  
    python manage.py runserver

🌐 Abre tu navegador favorito y ve a la dirección:

    http://127.0.0.1:8000/

    



