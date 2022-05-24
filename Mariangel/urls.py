"""Mariangel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from LogIn_SignUp.views import sign_up,eliminar_usuarios,log_in,log_out,account_info,forgot_password
from landing_page.views import init,basico,avanzado,full
from learning.views import secciones,contenidos,colores1,test_color1,colores2,test_color2,colores3,test_color3,colores4,test_color4,colores5,test_color5,colores6,test_color6,colores7,test_color7,abc,abc_test,palabras1,test_palabras,palabras2,test_palabras_2,family,seasons,saludos,test_saludos,bonus,contenidos
from Contacto.views import contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',init),
    path('registro/',sign_up),
    path('Inicio-Sesion/',log_in),
    path("eliminarUsers/",eliminar_usuarios),
    path("Salir-Sesion/",log_out),
    path("info/myaccount",account_info),
    path("OlvidarContrasenia/",forgot_password),
    path("Contacto/",contacto),
    #Aqui la url a Secciones
    path("Colores/1",colores1),
    path("tests/Colores/1",test_color1),
    path("Colores/2",colores2),
    path("tests/Colores/2",test_color2),
    path("Colores/3",colores3),
    path("tests/Colores/3",test_color3),
    path("Colores/4",colores4),
    path("tests/Colores/4",test_color4),
    path("Colores/5",colores5),
    path("tests/Colores/5",test_color5),
    path("Colores/6",colores6),
    path("tests/Colores/6",test_color6),
    path("Colores/7",colores7),
    path("tests/Colores/7",test_color7),
    path("ABC/1",abc),
    path("Secciones/",secciones),
    path("tests/ABC/1",abc_test),
    path("Palabras/1",palabras1),
    path("tests/Palabras/1",test_palabras),
    path("Palabras/2",palabras2),
    path("tests/Palabras/2",test_palabras_2),
    path("Frases/1",family),
    path("Frases/2",seasons),
    path("Frases/3",saludos),
    path("tests/Frases/3",test_saludos),
    path("Bonus/",bonus),
    path("Contenidos/",contenidos),
    #Url de planes
    path("Basico/",basico),
    path("Avanzado/",avanzado),
    path("Full/",full),
    #Url de contenidos
    path("Contenidos",contenidos)
]




