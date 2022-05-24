from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
#from LogIn_SignUp.util.log import aut_log
from LogIn_SignUp.views import get_user_logged_first_char
from Contacto.models import Contacto
from LogIn_SignUp.models import User
from django.contrib.auth.decorators import login_required
# Create your views here

@login_required
def contacto(request):
    if request.method =="POST":
        email_from = request.POST["email_from"]
        comentario = request.POST["comentario"]
        titulo = request.POST["titulo"]
        telefono = request.POST["telefono"]
        if len(titulo)>70:
            return HttpResponseRedirect("Contacto/")
        contacto = Contacto(username=request.user.username,email_from = email_from,comentario = comentario, titulo = titulo,telefono = telefono)
        contacto.save()
        return render(request,"Gracias.html")
    else:
        return render(request,"Contacto.html",{"initial_username":get_user_logged_first_char(request)})