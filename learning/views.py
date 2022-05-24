from cmath import log
from django.http import HttpResponse
from django.shortcuts import render
from numpy import var
from LogIn_SignUp.models import User
#from LogIn_SignUp.util.log import aut_log
from django.http import HttpResponseRedirect
from LogIn_SignUp.views import get_user_logged_first_char
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.


#Vista para secciones
def get_user(request_obj):
    for user in User.objects.all():
        if request_obj.user == user.user:
            return user
@login_required
def secciones(request):    
    usuario =get_user(request)
    color = usuario.last_video_color

    abc = usuario.last_video_abc

    simple_phrases = usuario.last_video_simple_phrases

    simple_words = usuario.last_video_simple_words

    color_true = color if color>1 else 1
    abc_true = abc if abc>1 else 1
    simple_phrases_true = simple_phrases if simple_phrases>1 else 1
    simple_words_true = simple_words if simple_words>1 else 1

    if usuario.has_been_tested_color and color!=0 and color!=7:
        color_true+=1
    if usuario.has_been_tested_abc and abc!=0 and abc!=1:
        abc_true+=1
    if usuario.has_been_tested_simple_phrases and simple_phrases!=0 and simple_phrases!=3:
        simple_phrases_true+=1
    if usuario.has_been_tested_simple_words and simple_words!=0 and simple_words!=2:
        simple_words_true+=1

    return render(request,"secciones.html",
    {"initial_username":get_user_logged_first_char(request),
        "color":color_true,
        "abc":abc_true,
        "simple_prases":simple_phrases_true,
        "simple_words":simple_words_true,
    })
@login_required
def contenidos(request):
    return render(request,"contenidos.html",{"initial_username":get_user_logged_first_char(request)})

@login_required
def colores1(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 0:
        user.last_video_color = 1
        user.has_been_tested_color = False
        user.save()
        return render(request,"color1.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color > 0:
        return render(request,"color1.html",{"initial_username":get_user_logged_first_char(request)})
@csrf_exempt
@login_required
def test_color1(request):
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/2")
    else:
        if user.last_video_color!=0:
            if user.last_video_color ==1:
                return render(request,"Yellow.html")
            elif user.last_video_color>1:
                return render(request,"Yellow.html")
            else:
                return HttpResponseRedirect("/Colores/1")
        else:
            return HttpResponseRedirect("/Colores/1")
@login_required
def colores2(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 1 and user.has_been_tested_color:
        user.last_video_color = 2
        user.has_been_tested_color = False
        user.save()
        return render(request,"color2.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color>=2:
        return render(request,"color2.html",{"initial_username":get_user_logged_first_char(request)})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")

@csrf_exempt
@login_required
def test_color2(request):
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/3")
    else:
        if user.last_video_color:
            if user.last_video_color ==2:
                user.has_been_tested_color = True
                user.save()
                return render(request,"Blue.html")
            elif user.last_video_color >2:
                return render(request,"Blue.html")
            else:
                return HttpResponseRedirect("/Colores/2")
        else:
            return HttpResponseRedirect("/Colores/1")
@login_required
def colores3(request):
    #Cojer el log automatico
    user = get_user(request)
    
    if user.last_video_color == 2 and user.has_been_tested_color and user.plan>=1:
        user.last_video_color = 3
        user.has_been_tested_color = False
        user.save()
        return render(request,"color3.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color>=3 and user.plan>=1:
        return render(request,"color3.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.plan <1:
        return render(request,"ComprarPlan.html",{"plan":"Avanzado"})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")
@csrf_exempt
@login_required
def test_color3(request):

    #Cojer el log automatico
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/4")
    else:
        if user.last_video_color:
            if user.last_video_color ==3:
                user.has_been_tested_color = True
                user.save()
                return render(request,"Red.html")
            elif user.last_video_color >2:
                return render(request,"Red.html")
            else:
                return HttpResponseRedirect("/Colores/3")
        else:
            return HttpResponseRedirect("/Colores/1")
#4
@login_required
def colores4(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 3 and user.has_been_tested_color and user.plan>=1:
        user.last_video_color = 4
        user.has_been_tested_color = False
        user.save()
        return render(request,"color4.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color>=4 and user.plan>=1:
        return render(request,"color4.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.plan <1:
        return render(request,"ComprarPlan.html",{"plan":"Avanzado"})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")
@csrf_exempt
@login_required
def test_color4(request):
    #Cojer el log automatico
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/5")
    else:
        if user.last_video_color:
            if user.last_video_color ==4:
                user.has_been_tested_color = True
                user.save()
                return render(request,"Green.html")
            elif user.last_video_color >3:
                return render(request,"Green.html")
            else:
                return HttpResponseRedirect("/Colores/4")
        else:
            return HttpResponseRedirect("/Colores/1")
#5
@login_required
def colores5(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 4 and user.has_been_tested_color and user.plan==2:
        user.last_video_color = 5
        user.has_been_tested_color = False
        user.save()
        return render(request,"color5.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color>=5 and user.plan == 2:
        return render(request,"color5.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.plan <2:
        return render(request,"ComprarPlan.html",{"plan":"Full"})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")
@csrf_exempt
@login_required
def test_color5(request):
    #Cojer el log automatico
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/6")
    else:
        if user.last_video_color:
            if user.last_video_color ==5:
                user.has_been_tested_color = True
                user.save()
                return render(request,"Pink.html")
            elif user.last_video_color >5:
                return render(request,"Pink.html")
            else:
                return HttpResponseRedirect("/Colores/5")
        else:
            return HttpResponseRedirect("/Colores/1")
#6
@login_required
def colores6(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 5 and user.has_been_tested_color and user.plan == 2:
        user.last_video_color = 6
        user.has_been_tested_color = False
        user.save()
        return render(request,"color6.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.last_video_color>=6 and user.plan == 2:
        return render(request,"color6.html",{"initial_username":get_user_logged_first_char(request)})
    elif user.plan <2:
        return render(request,"ComprarPlan.html",{"plan":"Full"})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")
@csrf_exempt
@login_required
def test_color6(request):
    #Cojer el log automatico
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_color = True
        user.save()
        return HttpResponseRedirect("/Colores/7")
    else:
        if user.last_video_color:
            if user.last_video_color ==6:
                user.has_been_tested_color = True
                user.save()
                return render(request,"Simultanea.html")
            elif user.last_video_color >6:
                return render(request,"Simultanea.html")
            else:
                return HttpResponseRedirect("/Colores/6")
        else:
            return HttpResponseRedirect("/Colores/1")
#7
@login_required
def colores7(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color == 6 and user.has_been_tested_color and user.plan == 2:
        user.last_video_color = 7
        user.has_been_tested_color = False
        user.save()
        return render(request,"color7.html")
    elif user.plan <2:
        return render(request,"ComprarPlan.html",{"plan":"Full"})
    elif user.last_video_color ==7 and user.plan == 2:
        return render(request,"color7.html",{"initial_username":get_user_logged_first_char(request)})
    else:
        return HttpResponse("No haz completado los tests anteriores o no los haz visto")
@csrf_exempt
@login_required
def test_color7(request):
    #Cojer el log automatico
    user = get_user(request)
    if user.last_video_color:
        if user.last_video_color ==7:
            user.has_been_tested_color = True
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("/Colores/7")
    else:
        return HttpResponseRedirect("/Colores/1")




@login_required
def abc(request):
    user = get_user(request)
    return render(request,"abc.html",{"initial_username":get_user_logged_first_char(request)})

@csrf_exempt
@login_required
def abc_test(request):
    if request.method == "POST":
        if "submit_bueno" in request.POST:
            return HttpResponseRedirect("/Secciones")
        else:
            return HttpResponseRedirect("/ABC/1")
    return render(request,"abc_test.html")
@login_required
def palabras1(request):
    user = get_user(request)
    if user.last_video_simple_words == 0:
        user.last_video_simple_words+=1
        user.has_been_tested_simple_words = False
        user.save()
        return render(request,"words1.html",{"initial_username":get_user_logged_first_char(request)})
    else:
        return render(request,"words1.html",{"initial_username":get_user_logged_first_char(request)})
@csrf_exempt
@login_required
def test_palabras(request):
    user = get_user(request)
    if user.last_video_simple_words>=1:
        if request.method == "POST":
            if "bueno" in request.POST:
                user.has_been_tested_simple_words = True
                user.save()
                return HttpResponseRedirect("/Palabras/2")
            else:
                return render(request, "words1_test.html")
        else:
            return render(request, "words1_test.html")
    else:
        return HttpResponseRedirect("/Palabras/1")
@login_required
def palabras2(request):
    user = get_user(request)
    if user.plan == 2:
        if user.last_video_simple_words == 1:
            if user.has_been_tested_simple_words:
                user.last_video_simple_words+=1
                return render(request,"words2.html",{"initial_username":get_user_logged_first_char(request)})
            else:
                return HttpResponseRedirect("/tests/Palabras/1")
        else:
            return HttpResponseRedirect("/Palabras/1")
    else:
        return render(request,"ComprarPlan.html",{"plan":"Full"})

@csrf_exempt
@login_required
def test_palabras_2(request):
    user = get_user(request)
    if user.last_video_simple_words == 1 and user.plan == 2:
        if request.method == "POST":
            if "bueno" in request.POST:
                user.has_been_tested_simple_words = True
                user.save()
                return HttpResponseRedirect("/Secciones")
            else:
                return render(request, "words2_test.html")
        else:
            return render(request, "words2_test.html")
    else:
        return HttpResponseRedirect("/Palabras/2")

@login_required
def family(request):
    user = get_user(request)
    if user.last_video_simple_phrases == 0:
        user.last_video_simple_phrases+=1
        user.has_been_tested_simple_phrases = True
        user.save()
        return render(request,"family.html",{"initial_username":get_user_logged_first_char(request)})
    else:
        return render(request,"family.html",{"initial_username":get_user_logged_first_char(request)})
@login_required
def seasons(request):
    user = get_user(request)
    if user.plan >=1:    
        if user.last_video_simple_phrases == 1:
            user.last_video_simple_phrases+=1
            user.has_been_tested_simple_phrases = True
            user.save()
            return render(request,"seasons.html",{"initial_username":get_user_logged_first_char(request)})
        elif user.last_video_simple_phrases > 1:
            return render(request,"seasons.html",{"initial_username":get_user_logged_first_char(request)})
        else:
            return HttpResponseRedirect("/Frases/1")
    else:
        return HttpResponse("<h1>Cambiese al plan <a href = '/#planes'>Avanzado</a></h1>")
@login_required
def saludos(request):
    user = get_user(request)
    if user.plan ==2:
        if user.last_video_simple_phrases == 2:
            user.last_video_simple_phrases +=1
            user.has_been_tested_simple_phrases = False
            user.save()
            return render(request,"saludos.html",{"initial_username":get_user_logged_first_char(request)})
        elif user.last_video_simple_phrases == 3:
            return render(request,"saludos.html",{"initial_username":get_user_logged_first_char(request)})
        else:
            return HttpResponseRedirect("/Frases/1")
    else:
        return render(request,"ComprarPlan.html",{"plan":"Full"})
@csrf_exempt
@login_required
def test_saludos(request):
    user = get_user(request)
    if request.method == "POST":
        user.has_been_tested_simple_phrases = True
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,"saludos_test.html")

@login_required
def bonus(request):
    user = get_user(request)
    if user == -1:
        return HttpResponseRedirect("/Inicio-Sesion/",{"initial_username":get_user_logged_first_char(request)})
    elif user is None:
        return HttpResponseRedirect("/registro/",{"initial_username":get_user_logged_first_char(request)})
    else:
        return render(request,"bonus.html",{"initial_username":get_user_logged_first_char(request)})
        
