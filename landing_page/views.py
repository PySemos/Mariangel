from django.shortcuts import render
from django.http import HttpResponseRedirect
from LogIn_SignUp.views import get_user_logged_first_char
from django.contrib.auth.decorators import login_required
from learning.views import get_user
# Create your views here.

@login_required
def init(request):
    return render(request,"index.html",{"initial_username":get_user_logged_first_char(request)})
@login_required
def basico(request):
    user = get_user(request)
    user.plan = 0
    user.save()
    return HttpResponseRedirect("/")

@login_required
def avanzado(request):
    user = get_user(request)
    user.plan = 1
    user.save()
    return HttpResponseRedirect("/")
    
@login_required
def full(request):
    user = get_user(request)
    user.plan = 2
    user.save()
    return HttpResponseRedirect("/")