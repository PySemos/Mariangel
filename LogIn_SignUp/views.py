from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from LogIn_SignUp.models import User
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
email_username_from_change_password = 0
def get_user_logged_first_char(request_obj):
    try:
        return request_obj.user.username[0]
    except IndexError:
        return

@csrf_exempt
def sign_up(request):
    if request.method =="POST":
        for user in DjangoUser.objects.all():
            if user.username == request.POST["username"]:
                return render(request,"sign_up.html",{"email_ok":True,"username_ok":False})
            if user.username == request.POST["email"]:
                return render(request,"sign_up.html",{"email_ok":False,"username_ok":True})
        dj_usuario = DjangoUser.objects.create(username = request.POST["username"],email = request.POST["email"],last_name = request.POST["lastname"])
        dj_usuario.set_password(request.POST["password"])
        dj_usuario.save()
        usuario = User(user = dj_usuario,age = request.POST["age"],ci = request.POST["ID"])
        usuario.save()
        login(request,usuario.user)
        return HttpResponseRedirect("/")
    else:
        return render(request,"sign_up.html",{"email_ok":True,"username_ok":True,"initial_username":get_user_logged_first_char(request)})

@csrf_exempt
def log_in(request):
    if request.method=="POST":
        usuario = authenticate(request,username = request.POST["username"],password = request.POST["password"])
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect("/")
        else:
            return render(request,"log_in.html",{"initial_username":get_user_logged_first_char(request),"OK":False})
    else:
        return render(request,"log_in.html",{"initial_username":get_user_logged_first_char(request),"OK":True})

@login_required        
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/Inicio-Sesion/")

@login_required
def account_info(request):
    usuario = None
    for user in User.objects.all():
        if user.user == request.user:
            usuario = user
    planes = ["Basico","Avanzado","Full",]
    return render(request,"info_account.html",{
        "initial_username":get_user_logged_first_char(request),
        "username":request.user.username,
        "email":request.user.email,
        "apellido":request.user.last_name,
        "id":usuario.ci,
        "age":usuario.age,
        "plan":planes[usuario.plan],
    })
@csrf_exempt
def forgot_password(request):
    if request.method =="POST":
        for user in User.objects.all():
            if request.POST["test_email_username"] == user.user.username or request.POST["test_email_username"] == user.user.email:
                if request.POST["ID"] == user.ci:
                    if request.POST["change_password"] == request.POST["change_password_again"] :
                        user.user.set_password(request.POST["change_password"])
                        user.user.save()
                        return HttpResponseRedirect("/Inicio-Sesion")
                    else:
                        return render(request,"olvidar_contrasenia.html",{"wrong_password_again":True,"initial_username":get_user_logged_first_char(request)})
                else:
                    return render(request,"olvidar_contrasenia.html",{"initial_username":get_user_logged_first_char(request),"wrong_aut":True}) 
        return render(request,"olvidar_contrasenia.html",{"initial_username":get_user_logged_first_char(request),"wrong_aut":True}) 
    else:
        return render(request,"olvidar_contrasenia.html",{
            "initial_username":get_user_logged_first_char(request),
            "wrong_aut":False,
        })

def eliminar_usuarios(request):
    return HttpResponseRedirect("/")


